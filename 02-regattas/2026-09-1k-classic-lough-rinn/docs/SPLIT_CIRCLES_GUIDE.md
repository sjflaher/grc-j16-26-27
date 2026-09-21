# Split-Circle Visualization Guide

## Overview

The regatta visualization now uses **two-color split circles** for clubs that have multiple official colors, making them much easier to distinguish at a glance.

## Visual Design

### Split Circles (24 clubs)

For clubs with primary AND secondary colors:

```
Left Half  | Right Half
-----------+-----------
Primary    | Secondary
```

**Example: Galway Rowing Club**
```
    ◐
   ◐ ◑     ← Left: Purple (#800080)
  ◐   ◑    ← Right: Amber (#FFBF00)
   ◐ ◑
    ◐
```

**Example: Enniskillen**
```
    ◐
   ◐ ◑     ← Left: Blue (#0066CC)
  ◐   ◑    ← Right: Red (#DC143C)
   ◐ ◑
    ◐
```

**Example: St. Michaels**
```
    ◐
   ◐ ◑     ← Left: Royal Blue (#4169E1)
  ◐   ◑    ← Right: Old Gold (#CFB53B)
   ◐ ◑
    ◐
```

### Solid Circles (4 clubs)

For clubs with only one color:

```
    ●
   ● ●     ← Single color throughout
  ● ● ●
   ● ●
    ●
```

**Example: Shandon (Light Blue)**
**Example: St Josephs (Blue)**

## Size Hierarchy

- **Galway crews**: 22px diameter (LARGE)
  - Makes Galway stand out clearly
  - Still shows both purple and amber colors
  
- **Other crews**: 12px diameter (standard)
  - Smaller but still clearly shows split colors
  - Easy to scan across the chart

- **On hover**: +6px expansion
  - Galway: 22px → 28px
  - Others: 12px → 16px

## Clubs with Split Circles

### Your Regatta (24 clubs with 2 colors)

| Club | Left Half | Right Half | Description |
|------|-----------|------------|-------------|
| **Galway** ⭐ | Purple #800080 | Amber #FFBF00 | Purple & Amber |
| Enniskillen | Blue #0066CC | Red #DC143C | Blue & Red |
| Methodist | Navy #000080 | White #FFFFFF | Navy Blue/White |
| Athlone | Green #228B22 | Red #DC143C | Green & Red |
| Castleconnel | Red #DC143C | Grey #808080 | Red & Grey |
| Col Iognaid | Maroon #800000 | White #FFFFFF | Maroon & White |
| Pres Cork | Black #000000 | White #FFFFFF | Black, White Hoops, Purple Trim |
| St. Michaels | Royal Blue #4169E1 | Old Gold #CFB53B | Royal Blue & Old Gold |
| Bann | Red #DC143C | White #FFFFFF | Red & White |
| Commercial | Myrtle Green #317873 | White #FFFFFF | Myrtle Green, White & Azure Blue |
| Cork | Chocolate #3F2212 | White #FFFFFF | Chocolate Brown & White |
| CRCC | Teal #008080 | Black #000000 | Teal, Black & White |
| Fermoy | White #FFFFFF | Green #228B22 | White & Green Hoops |
| Lee | Red #DC143C | Black #000000 | Red & Black |
| Newry | Red #DC143C | Black #000000 | Red & Black with Yellow Star |
| Northwest | Blue #0066CC | White #FFFFFF | Blue & White |
| Offaly | Grey #808080 | Red #DC143C | Grey & Red |
| Skibbereen | Red #DC143C | White #FFFFFF | Red & White |
| Sligo | Black #000000 | Red #DC143C | Black and Red |
| Waterford | Navy #000080 | White #FFFFFF | Navy & White Hoop |

## Visual Benefits

### Before (Single Color)
```
🟣 Galway
🟣 Enniskillen
🟣 Methodist
...all looked similar except for subtle shade differences
```

### After (Split Circles)
```
◐ Galway (Purple | Amber)
◐ Enniskillen (Blue | Red)
◐ Methodist (Navy | White)
...instantly distinguishable!
```

## Technical Implementation

### Canvas-Based Point Rendering

Each point is drawn on a custom Canvas element:

1. **Split Circle**:
   - Left semicircle: Primary color (0.5π to 1.5π)
   - Right semicircle: Secondary color (1.5π to 0.5π)
   - Subtle border: `rgba(0,0,0,0.15)`
   - Center dividing line: `rgba(0,0,0,0.2)`

2. **Solid Circle**:
   - Full circle: Primary color (0 to 2π)
   - Subtle border: `rgba(0,0,0,0.15)`

### Chart.js Integration

```javascript
// Generate custom point style
if (hasSecondary) {
    pointStyle = createSplitCirclePoint(primary, secondary, 12);
} else {
    pointStyle = createSolidCirclePoint(primary, 12);
}

// Apply to dataset
datasets.push({
    pointStyle: pointStyle,
    pointRadius: 6,  // Half of diameter
    // ...
});
```

## Color Combinations

### High Contrast (Easy to See)
- **Galway**: Purple | Amber
- **Enniskillen**: Blue | Red
- **St. Michaels**: Royal Blue | Old Gold
- **Athlone**: Green | Red
- **Lee**: Red | Black
- **Sligo**: Black | Red

### Subtle (But Still Clear)
- **Methodist**: Navy | White
- **Castleconnel**: Red | Grey
- **Commercial**: Myrtle Green | White
- **Cork**: Chocolate Brown | White

## Usage in Analysis

### Pattern Recognition

Now you can instantly spot:

1. **Galway crews** (large purple/amber split)
   - Easy to track across all 6 events
   - See placement relative to competitors

2. **Red-based clubs** (Red | X pattern)
   - Bann, Castleconnel, Lee, Newry, Skibbereen
   - Compare performance across red clubs

3. **Blue-based clubs** (Blue | X pattern)
   - Enniskillen, Methodist, Northwest
   - See clustering patterns

4. **White-dominant clubs** (White | X pattern)
   - Fermoy (white/green hoops)
   - Easy to spot light-colored markers

### Competitive Analysis

"I can see Enniskillen (blue/red) dominating the top ranks, while Galway (purple/amber) sits mid-pack but benefits from heat adjustments"

The split colors make this kind of multi-club comparison effortless.

## Files

- **Visualization**: `regatta-visualization-colored.html`
- **Color database**: `club_colors.json`
- **This guide**: `SPLIT_CIRCLES_GUIDE.md`

---

**Pro Tip**: The split-circle design is based on traditional rowing club colors where the oar blades often feature two-color patterns. This visualization honors that heritage!
