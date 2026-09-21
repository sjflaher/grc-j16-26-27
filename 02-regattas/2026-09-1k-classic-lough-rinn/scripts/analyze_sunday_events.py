#!/usr/bin/env python3
"""
Analyze Sunday regatta events with heat adjustment for Galway crews.
Events: M J15 4x+ (races 205-210), M J15 2x (races 233-241), M J14 2x (races 258-264)
"""

import csv
import statistics
import re
from collections import defaultdict

def time_to_seconds(time_str):
    """Convert MM:SS.S format to seconds"""
    if not time_str or time_str in ['DNS', 'DNF', 'NTT', '']:
        return None
    time_str = time_str.strip()
    if ':' not in time_str:
        return None
    try:
        parts = time_str.split(':')
        minutes = int(parts[0])
        seconds = float(parts[1])
        return minutes * 60 + seconds
    except:
        return None

def format_time(seconds):
    """Convert seconds to MM:SS.S format"""
    if seconds is None:
        return "DNS"
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}:{secs:04.1f}"

def parse_regatta_csv(filepath):
    """Parse the regatta CSV format"""
    events = defaultdict(list)
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Parse race header line
        parts = line.split(',')
        if len(parts) < 5:
            i += 1
            continue
            
        race_no = parts[0].strip('"')
        if not race_no.isdigit():
            i += 1
            continue
            
        race_no = int(race_no)
        event_name = parts[3].strip('"') if len(parts) > 3 else ""
        heat_type = parts[4].strip('"') if len(parts) > 4 else ""
        
        # Get crew names from header (lanes 1-6)
        crews = {}
        for lane in range(1, 7):
            idx = 5 + (lane - 1) * 2  # Crew names at positions 5, 7, 9, 11, 13, 15
            if idx < len(parts):
                crew_name = parts[idx].strip('"').strip()
                if crew_name:
                    crews[lane] = crew_name
        
        # Next line has results
        i += 1
        if i < len(lines):
            results_line = lines[i].strip()
            result_parts = results_line.split(',')
            
            # Parse times - format: [position],time for each lane
            for lane in range(1, 7):
                idx = 5 + (lane - 1) * 2  # Position at 5, 7, 9, 11, 13, 15
                time_idx = idx + 1  # Time at 6, 8, 10, 12, 14, 16
                
                if time_idx < len(result_parts) and lane in crews:
                    position_str = result_parts[idx].strip('"[]')
                    time_str = result_parts[time_idx].strip('"')
                    
                    time_seconds = time_to_seconds(time_str)
                    if time_seconds is not None:
                        events[(event_name, race_no)].append({
                            'crew': crews[lane],
                            'time': time_seconds,
                            'raw_time': time_str,
                            'lane': lane,
                            'race': race_no,
                            'heat': heat_type,
                            'position': position_str if position_str.isdigit() else None
                        })
        i += 1
    
    return events

def analyze_event(events_data, event_name, race_range, galway_crews_expected):
    """Analyze a specific event with heat adjustment"""
    
    print("\n" + "=" * 90)
    print(f"{event_name} HEAT ADJUSTMENT ANALYSIS")
    print(f"Races {race_range[0]}-{race_range[-1]} ({len(race_range)} Finals)")
    print("=" * 90)
    
    # Collect all results for this event
    all_results = []
    heats = defaultdict(list)
    
    for race_no in race_range:
        for key, results in events_data.items():
            if key[1] == race_no:
                for r in results:
                    r['event'] = event_name
                    all_results.append(r)
                    heats[r['heat']].append(r)
    
    if not all_results:
        print(f"No results found for races {race_range}")
        return None
    
    # Find Galway crews
    galway_results = [r for r in all_results if 'Galway' in r['crew']]
    
    print(f"\nLoaded {len(all_results)} crews across {len(heats)} finals")
    print(f"Galway crews found: {len(galway_results)}")
    for g in galway_results:
        print(f"  - {g['crew']} in {g['heat']} (Race {g['race']})")
    
    # Heat statistics
    print("\n" + "-" * 90)
    print("HEAT STATISTICS")
    print("-" * 90)
    
    overall_times = [r['time'] for r in all_results]
    overall_mean = statistics.mean(overall_times)
    
    print(f"\nOverall mean time: {format_time(overall_mean)}")
    print(f"\n{'Heat':<15} {'Count':<8} {'Mean':<12} {'Median':<12} {'Std Dev':<10}")
    print("-" * 60)
    
    heat_stats = {}
    for heat_name in sorted(heats.keys()):
        times = [r['time'] for r in heats[heat_name]]
        mean_time = statistics.mean(times)
        median_time = statistics.median(times)
        stdev = statistics.stdev(times) if len(times) > 1 else 0
        heat_stats[heat_name] = {
            'mean': mean_time,
            'median': median_time,
            'stdev': stdev,
            'count': len(times),
            'adjustment': mean_time - overall_mean
        }
        print(f"{heat_name:<15} {len(times):<8} {format_time(mean_time):<12} {format_time(median_time):<12} {stdev:<10.2f}")
    
    # Heat speed range
    means = [s['mean'] for s in heat_stats.values()]
    heat_range = max(means) - min(means)
    fastest_heat = min(heat_stats.keys(), key=lambda h: heat_stats[h]['mean'])
    slowest_heat = max(heat_stats.keys(), key=lambda h: heat_stats[h]['mean'])
    
    print(f"\nFastest heat: {fastest_heat} ({format_time(heat_stats[fastest_heat]['mean'])} average)")
    print(f"Slowest heat: {slowest_heat} ({format_time(heat_stats[slowest_heat]['mean'])} average)")
    print(f"Heat speed range: {heat_range:.1f}s")
    
    # RAW RANKINGS
    print("\n" + "-" * 90)
    print("RAW TIMES (No Adjustments)")
    print("-" * 90)
    
    raw_sorted = sorted(all_results, key=lambda x: x['time'])
    
    print(f"\n{'Rank':<6} {'Crew':<35} {'Heat':<15} {'Time':<10}")
    print("-" * 70)
    
    galway_raw_ranks = {}
    for i, r in enumerate(raw_sorted, 1):
        galway_marker = " ← GALWAY" if 'Galway' in r['crew'] else ""
        print(f"{i:<6} {r['crew']:<35} {r['heat']:<15} {format_time(r['time']):<10}{galway_marker}")
        if 'Galway' in r['crew']:
            galway_raw_ranks[r['crew']] = i
    
    # HEAT-ADJUSTED RANKINGS
    print("\n" + "-" * 90)
    print("HEAT-ADJUSTED TIMES (Mean Method)")
    print("-" * 90)
    print("Adjusted = Raw - (Heat Mean - Overall Mean)")
    
    for r in all_results:
        heat_adj = heat_stats[r['heat']]['adjustment']
        r['adjusted_time'] = r['time'] - heat_adj
        r['heat_adjustment'] = heat_adj
    
    adj_sorted = sorted(all_results, key=lambda x: x['adjusted_time'])
    
    print(f"\n{'Rank':<6} {'Crew':<35} {'Heat':<15} {'Raw':<10} {'Adj':<10} {'Heat Adj':<10}")
    print("-" * 90)
    
    galway_adj_ranks = {}
    for i, r in enumerate(adj_sorted, 1):
        galway_marker = " ← GALWAY" if 'Galway' in r['crew'] else ""
        adj_str = f"{r['heat_adjustment']:+.1f}s"
        print(f"{i:<6} {r['crew']:<35} {r['heat']:<15} {format_time(r['time']):<10} {format_time(r['adjusted_time']):<10} {adj_str:<10}{galway_marker}")
        if 'Galway' in r['crew']:
            galway_adj_ranks[r['crew']] = i
    
    # GALWAY SUMMARY
    print("\n" + "-" * 90)
    print("GALWAY CREWS SUMMARY")
    print("-" * 90)
    
    galway_summary = []
    for g in galway_results:
        crew = g['crew']
        raw_rank = galway_raw_ranks.get(crew, '?')
        adj_rank = galway_adj_ranks.get(crew, '?')
        rank_change = raw_rank - adj_rank if isinstance(raw_rank, int) and isinstance(adj_rank, int) else 0
        
        print(f"\n{crew}:")
        print(f"  Heat: {g['heat']} (Race {g['race']})")
        print(f"  Raw Time: {format_time(g['time'])} (Rank {raw_rank})")
        print(f"  Heat Adjustment: {g['heat_adjustment']:+.1f}s ({'faster' if g['heat_adjustment'] < 0 else 'slower'} heat)")
        print(f"  Adjusted Time: {format_time(g['adjusted_time'])} (Rank {adj_rank})")
        print(f"  Position Change: {rank_change:+d} places")
        
        galway_summary.append({
            'crew': crew,
            'heat': g['heat'],
            'raw_time': g['time'],
            'raw_rank': raw_rank,
            'adj_time': g['adjusted_time'],
            'adj_rank': adj_rank,
            'change': rank_change
        })
    
    return {
        'event': event_name,
        'total_crews': len(all_results),
        'heats': len(heats),
        'heat_range': heat_range,
        'galway': galway_summary
    }

def main():
    filepath = "/tmp/sunday_regatta.csv"
    events_data = parse_regatta_csv(filepath)
    
    print("=" * 90)
    print("ROWING IRELAND 1K CLASSIC 2026 - SUNDAY RESULTS")
    print("Heat Adjustment Analysis for Galway Crews")
    print("=" * 90)
    
    summaries = []
    
    # M J15 4x+ (races 205-210)
    result = analyze_event(events_data, "M J15 4x+", range(205, 211), 2)
    if result:
        summaries.append(result)
    
    # M J15 2x (races 233-241)
    result = analyze_event(events_data, "M J15 2x", range(233, 242), 2)
    if result:
        summaries.append(result)
    
    # M J14 2x (races 258-264 based on the data, but user said 261-264)
    result = analyze_event(events_data, "M J14 2x", range(258, 265), 1)
    if result:
        summaries.append(result)
    
    # Final summary
    print("\n" + "=" * 90)
    print("OVERALL GALWAY SUMMARY - SUNDAY EVENTS")
    print("=" * 90)
    
    for s in summaries:
        print(f"\n{s['event']}: {s['total_crews']} crews across {s['heats']} finals, {s['heat_range']:.1f}s heat variation")
        for g in s['galway']:
            print(f"  {g['crew']}: {g['raw_rank']} → {g['adj_rank']} ({g['change']:+d})")

if __name__ == "__main__":
    main()
