#!/usr/bin/env python3
"""
Statistical methods for adjusting regatta times across heats.
Pure Python implementation (no external dependencies).
"""

import csv
import statistics
from datetime import datetime
import math

def load_data(csv_file):
    """Load race data from CSV"""
    heats = {}
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Time (MM:SS.S)'] == 'DNS':
                continue
            heat = row['Heat']
            if heat not in heats:
                heats[heat] = []
            heats[heat].append({
                'crew': row['Crew'],
                'time': float(row['Time (Seconds)']),
                'raw_time': row['Time (MM:SS.S)'],
                'race': row['Race Number'],
                'lane': row['Lane']
            })
    return heats

def percentile_of_score(data, score):
    """Calculate percentile of a score in a dataset"""
    below = sum(1 for x in data if x < score)
    equal = sum(1 for x in data if x == score)
    return (below + 0.5 * equal) / len(data) * 100

def percentile_value(data, pct):
    """Get value at percentile"""
    data_sorted = sorted(data)
    k = (len(data) - 1) * (pct / 100.0)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return data_sorted[int(k)]
    d0 = data_sorted[int(f)] * (c - k)
    d1 = data_sorted[int(c)] * (k - f)
    return d0 + d1

def ttest_independent(data1, data2):
    """Independent samples t-test"""
    n1, n2 = len(data1), len(data2)
    mean1, mean2 = statistics.mean(data1), statistics.mean(data2)
    var1 = statistics.variance(data1) if n1 > 1 else 0
    var2 = statistics.variance(data2) if n2 > 1 else 0
    
    # Pooled standard deviation
    pooled_var = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)
    pooled_std = math.sqrt(pooled_var)
    
    # t-statistic
    se = math.sqrt(pooled_var * (1/n1 + 1/n2))
    t_stat = (mean1 - mean2) / se if se != 0 else 0
    
    # Degrees of freedom
    df = n1 + n2 - 2
    
    # Cohen's d
    cohens_d = abs(mean1 - mean2) / pooled_std if pooled_std != 0 else 0
    
    # Rough p-value approximation (for df > 30, use normal approximation)
    # For smaller df, this is approximate
    if df > 30:
        # Normal approximation
        p_value = 2 * (1 - 0.5 * (1 + math.erf(abs(t_stat) / math.sqrt(2))))
    else:
        # Rough approximation
        p_value = 0.05 if abs(t_stat) > 2.0 else 0.20  # Simplified
    
    return {
        't_stat': t_stat,
        'p_value': p_value,
        'cohens_d': cohens_d,
        'mean_diff': abs(mean1 - mean2),
        'df': df
    }

def format_time(seconds):
    """Convert seconds to MM:SS.S format"""
    if seconds >= 999:
        return "DNS"
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}:{secs:04.1f}"

def analyze_heats(csv_file):
    """Main analysis function"""
    heats = load_data(csv_file)
    
    print("\n" + "="*80)
    print("HEAT ADJUSTMENT ANALYSIS - M J15 8x+")
    print("="*80)
    
    # Calculate basic statistics
    all_times = []
    heat_stats = {}
    
    for heat_name, crews in heats.items():
        times = [c['time'] for c in crews]
        all_times.extend(times)
        heat_stats[heat_name] = {
            'mean': statistics.mean(times),
            'median': statistics.median(times),
            'stdev': statistics.stdev(times) if len(times) > 1 else 0,
            'count': len(times),
            'times': times
        }
    
    overall_mean = statistics.mean(all_times)
    overall_median = statistics.median(all_times)
    
    print(f"\nHeat Statistics:")
    print(f"{'Heat':<15} {'Mean':<12} {'Median':<12} {'Std Dev':<10} {'Count':<8}")
    print("-" * 60)
    for heat_name, stats in heat_stats.items():
        print(f"{heat_name:<15} {format_time(stats['mean']):<12} {format_time(stats['median']):<12} {stats['stdev']:<10.2f} {stats['count']:<8}")
    print(f"\n{'Overall':<15} {format_time(overall_mean):<12} {format_time(overall_median):<12}")
    
    # Statistical test
    if len(heats) == 2:
        print("\n" + "-"*80)
        print("STATISTICAL TEST: Are the two heats significantly different?")
        print("-"*80)
        
        heat_list = list(heats.values())
        times_1 = [c['time'] for c in heat_list[0]]
        times_2 = [c['time'] for c in heat_list[1]]
        
        test_result = ttest_independent(times_1, times_2)
        
        print(f"\nIndependent t-test:")
        print(f"  t-statistic: {test_result['t_stat']:.3f}")
        print(f"  Degrees of freedom: {test_result['df']}")
        print(f"  Mean difference: {test_result['mean_diff']:.2f} seconds")
        print(f"  Cohen's d (effect size): {test_result['cohens_d']:.3f}")
        
        # Interpretation
        if test_result['cohens_d'] < 0.2:
            effect = "negligible"
        elif test_result['cohens_d'] < 0.5:
            effect = "small"
        elif test_result['cohens_d'] < 0.8:
            effect = "medium"
        else:
            effect = "large"
        
        print(f"\nEffect size interpretation: {effect}")
        
        if abs(test_result['t_stat']) > 2.0:
            print("\n✓ Heat differences appear STATISTICALLY SIGNIFICANT")
            print("  → Heat adjustment is recommended")
        else:
            print("\n✗ Heat differences are NOT statistically significant")
            print("  → Raw times may be fair, but adjustment still provides useful perspective")
    
    # Method 1: Heat Average Adjustment
    print("\n" + "="*80)
    print("METHOD 1: Heat Average Adjustment")
    print("="*80)
    print("Adjusts each time based on: Adjusted = Raw - (Heat Mean - Overall Mean)")
    print()
    
    avg_adjusted = []
    for heat_name, crews in heats.items():
        heat_adj = heat_stats[heat_name]['mean'] - overall_mean
        for crew in crews:
            avg_adjusted.append({
                **crew,
                'heat': heat_name,
                'adjusted_time': crew['time'] - heat_adj,
                'heat_adjustment': heat_adj
            })
    
    avg_adjusted.sort(key=lambda x: x['adjusted_time'])
    
    print(f"{'Rank':<6} {'Crew':<20} {'Heat':<12} {'Raw Time':<12} {'Adjusted':<12} {'Adjustment':<12}")
    print("-" * 85)
    
    for i, result in enumerate(avg_adjusted, 1):
        print(f"{i:<6} {result['crew']:<20} {result['heat']:<12} {result['raw_time']:<12} "
              f"{format_time(result['adjusted_time']):<12} {result['heat_adjustment']:>+6.2f}s")
    
    # Method 2: Median-Based Adjustment
    print("\n" + "="*80)
    print("METHOD 2: Median-Based Adjustment (More robust to outliers)")
    print("="*80)
    print("Adjusts each time based on: Adjusted = Raw - (Heat Median - Overall Median)")
    print()
    
    med_adjusted = []
    for heat_name, crews in heats.items():
        heat_adj = heat_stats[heat_name]['median'] - overall_median
        for crew in crews:
            med_adjusted.append({
                **crew,
                'heat': heat_name,
                'adjusted_time': crew['time'] - heat_adj,
                'heat_adjustment': heat_adj
            })
    
    med_adjusted.sort(key=lambda x: x['adjusted_time'])
    
    print(f"{'Rank':<6} {'Crew':<20} {'Heat':<12} {'Raw Time':<12} {'Adjusted':<12} {'Adjustment':<12}")
    print("-" * 85)
    
    for i, result in enumerate(med_adjusted, 1):
        print(f"{i:<6} {result['crew']:<20} {result['heat']:<12} {result['raw_time']:<12} "
              f"{format_time(result['adjusted_time']):<12} {result['heat_adjustment']:>+6.2f}s")
    
    # Method 3: Percentile
    print("\n" + "="*80)
    print("METHOD 3: Within-Heat Percentile Ranking")
    print("="*80)
    print("Converts times to percentiles within each heat, then maps to overall distribution")
    print()
    
    pct_adjusted = []
    for heat_name, crews in heats.items():
        heat_times = [c['time'] for c in crews]
        for crew in crews:
            percentile = percentile_of_score(heat_times, crew['time'])
            adjusted_time = percentile_value(all_times, percentile)
            pct_adjusted.append({
                **crew,
                'heat': heat_name,
                'adjusted_time': adjusted_time,
                'percentile': percentile
            })
    
    pct_adjusted.sort(key=lambda x: x['adjusted_time'])
    
    print(f"{'Rank':<6} {'Crew':<20} {'Heat':<12} {'Raw Time':<12} {'Percentile':<12} {'Adjusted':<12}")
    print("-" * 90)
    
    for i, result in enumerate(pct_adjusted, 1):
        print(f"{i:<6} {result['crew']:<20} {result['heat']:<12} {result['raw_time']:<12} "
              f"{result['percentile']:>5.1f}%      {format_time(result['adjusted_time']):<12}")
    
    # Galway-specific analysis
    print("\n" + "="*80)
    print("GALWAY ANALYSIS")
    print("="*80)
    
    for method_name, results in [("Heat Average", avg_adjusted), ("Median-Based", med_adjusted), ("Percentile", pct_adjusted)]:
        for i, r in enumerate(results, 1):
            if r['crew'] == 'Galway':
                print(f"\n{method_name} Adjustment:")
                print(f"  Raw rank: 9th (3:40.1)")
                print(f"  Adjusted rank: {i}{['th','st','nd','rd','th','th','th','th','th','th'][i%10 if i%10<4 and not 10<=i%100<=13 else 0]}")
                print(f"  Adjusted time: {format_time(r['adjusted_time'])}")
                if 'heat_adjustment' in r:
                    print(f"  Heat adjustment: {r['heat_adjustment']:+.2f} seconds")
                break
    
    # Recommendations
    print("\n" + "="*80)
    print("RECOMMENDATIONS")
    print("="*80)
    print("""
For rowing regattas with random heat seeding:

1. HEAT AVERAGE ADJUSTMENT (Method 1)
   - Most commonly used in rowing
   - Simple and transparent
   - Assumes random distribution of talent across heats
   - Best when heats are roughly equal size
   
2. MEDIAN-BASED ADJUSTMENT (Method 2)
   - More robust if one crew is much slower/faster than others
   - Good for small heats (3-6 crews)
   - Less affected by outliers
   
3. PERCENTILE RANKING (Method 3)
   - Best for larger heats (6+ crews)
   - Most robust to non-normal distributions
   - Loses some precision with very small heats

WHEN TO USE ADJUSTMENTS:
- If statistical tests show significance: Adjustments are justified
- If average times differ by >3 seconds: Consider adjustment
- If conditions (wind, water) were clearly different: Use adjustment
- For selection decisions: Show both raw and adjusted rankings

For this M J15 8x+ event:
- Heat 1 average: """ + format_time(heat_stats['Final 1']['mean']) + """
- Heat 2 average: """ + format_time(heat_stats['Final 2']['mean']) + """
- Difference: """ + f"{abs(heat_stats['Final 1']['mean'] - heat_stats['Final 2']['mean']):.2f}" + """ seconds

IMPORTANT: No statistical method can perfectly separate crew ability from 
conditions. Always consider:
- Recorded wind/water conditions
- Lane assignments (some lanes may be favored)
- Time of day effects (if heats run hours apart)
- Visual observations of rowing quality
""")
    
    return avg_adjusted

if __name__ == '__main__':
    csv_file = '/tmp/m_j15_8x_complete_analysis.csv'
    results = analyze_heats(csv_file)
