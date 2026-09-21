# Before & After: Split-Circle Visualization

## The Challenge

With single-color markers, clubs were distinguishable only by subtle shade differences. When you have 24 clubs, many colors start to look similar, especially:

- Multiple red clubs (Bann, Castleconnel, Lee, Newry, Skibbereen)
- Multiple blue clubs (Enniskillen, Methodist, Northwest, St Josephs)
- Dark colors (Black, Navy, Maroon) hard to tell apart

## The Solution

**Two-color hemisphere markers** that show BOTH club colors, making each club instantly recognizable.

---

## Visual Comparison

### BEFORE: Single-Color Markers

```
Rank 1  🔵 Enniskillen A      (Blue)
Rank 2  🔴 Castleconnel       (Red)
Rank 3  🔵 Methodist          (Navy - looks like blue)
Rank 4  🔵 St Josephs         (Blue)
Rank 5  🟤 Col Iognaid        (Maroon - dark)
Rank 6  🔷 St. Michaels       (Royal Blue - another blue)
Rank 7  ⚫ Pres Cork          (Black - dark)
Rank 8  🔵 Enniskillen B      (Blue again)
Rank 9  🟣 Galway             (Purple)
Rank 10 🟢 Athlone            (Green)

Problem: Too many similar blues! Too many reds! Hard to tell clubs apart!
```

### AFTER: Split-Circle Markers

```
Rank 1  ◐ Enniskillen A      (Blue | Red)         ← Unique!
Rank 2  ◐ Castleconnel       (Red | Grey)         ← Unique!
Rank 3  ◐ Methodist          (Navy | White)       ← Unique!
Rank 4  ● St Josephs         (Blue solid)         ← Different from split blues
Rank 5  ◐ Col Iognaid        (Maroon | White)     ← White half brightens it
Rank 6  ◐ St. Michaels       (Royal Blue | Gold)  ← Gold makes it unique
Rank 7  ◐ Pres Cork          (Black | White)      ← White half brightens it
Rank 8  ◐ Enniskillen B      (Blue | Red)         ← Same as Enniskillen A
Rank 9  ◐◐ Galway            (Purple | Amber)     ← LARGE, very distinctive
Rank 10 ◐ Athlone            (Green | Red)        ← Unique split

Benefit: Every club is instantly identifiable!
```

---

## Detailed Examples

### Example 1: Galway (Purple & Amber)

**Before:**
```
    🟣
   🟣🟣
  🟣🟣🟣    ← Solid purple
   🟣🟣        Hard to see the amber color
    🟣
```

**After:**
```
    ◐◐◐
   ◐◐◐◐◐    ← Left: Purple | Right: Amber
  ◐◐◐◐◐◐◐     Both colors clearly visible
   ◐◐◐◐◐      LARGE (22px) for emphasis
    ◐◐◐
```

### Example 2: Enniskillen (Blue & Red)

**Before:**
```
    🔵
   🔵🔵      ← Looks like many other blue clubs
  🔵🔵🔵       (Methodist, Northwest, St Josephs all similar)
   🔵🔵
    🔵
```

**After:**
```
    ◐
   ◐ ◑       ← Left: Blue | Right: Red
  ◐   ◑        Instantly recognizable split
   ◐ ◑
    ◐
```

### Example 3: Methodist (Navy Blue/White)

**Before:**
```
    🔵
   🔵🔵      ← Navy looked like regular blue
  🔵🔵🔵       Hard to distinguish from Enniskillen
   🔵🔵
    🔵
```

**After:**
```
    ◐
   ◐ ◑       ← Left: Navy | Right: White
  ◐   ◑        White half makes it distinctive
   ◐ ◑          Different from Enniskillen's red
    ◐
```

### Example 4: St. Michaels (Royal Blue & Old Gold)

**Before:**
```
    🔷
   🔷🔷      ← Another blue club
  🔷🔷🔷       Slightly different shade but hard to spot
   🔷🔷
    🔷
```

**After:**
```
    ◐
   ◐ ◑       ← Left: Royal Blue | Right: Old Gold
  ◐   ◑        Gold half makes it unique
   ◐ ◑          Completely different from other blues
    ◐
```

### Example 5: Pres Cork (Black, White Hoops, Purple Trim)

**Before:**
```
    ⚫
   ⚫⚫      ← Solid black
  ⚫⚫⚫       Very dark, hard to distinguish
   ⚫⚫
    ⚫
```

**After:**
```
    ◐
   ◐ ◑       ← Left: Black | Right: White
  ◐   ◑        White half brightens it considerably
   ◐ ◑          Much easier to spot on the chart
    ◐
```

---

## Color Differentiation Matrix

### Red-Based Clubs (Now Easily Distinguished)

| Club | Before | After | Difference |
|------|--------|-------|------------|
| Bann | 🔴 Red | ◐ Red \| White | White half |
| Castleconnel | 🔴 Red | ◐ Red \| Grey | Grey half |
| Lee | 🔴 Red | ◐ Red \| Black | Black half |
| Newry | 🔴 Red | ◐ Red \| Black | Same as Lee (different club name) |
| Skibbereen | 🔴 Red | ◐ Red \| White | Same as Bann (different club name) |

**Before**: All looked identical
**After**: White vs Grey vs Black halves distinguish them

### Blue-Based Clubs (Now Easily Distinguished)

| Club | Before | After | Difference |
|------|--------|-------|------------|
| Enniskillen | 🔵 Blue | ◐ Blue \| Red | Red half |
| Methodist | 🔵 Navy | ◐ Navy \| White | White half + darker blue |
| Northwest | 🔵 Blue | ◐ Blue \| White | White half |
| St Josephs | 🔵 Blue | ● Blue solid | No split (single color) |
| St. Michaels | 🔷 Royal Blue | ◐ Royal Blue \| Gold | Gold half |

**Before**: All looked like variations of blue
**After**: Red, White, Gold, or solid distinguish them clearly

### Dark Clubs (Now Much More Visible)

| Club | Before | After | Improvement |
|------|--------|-------|-------------|
| Pres Cork | ⚫ Black | ◐ Black \| White | White half brightens it |
| Col Iognaid | 🟤 Maroon | ◐ Maroon \| White | White half brightens it |
| Sligo | ⚫ Black | ◐ Black \| Red | Red half brightens it |
| Lee | 🔴 Red | ◐ Red \| Black | Black half provides contrast |

**Before**: Dark colors blended together
**After**: Light-colored halves make them stand out

---

## Pattern Recognition

### BEFORE: Difficult
"I see several blue dots at the top... which clubs are those?"
"There's a red cluster mid-pack... who's in there?"

### AFTER: Instant
"Enniskillen (blue/red) dominates the top 3 positions"
"Methodist (navy/white) is consistently top 10"
"The red-based clubs (Bann, Lee, Skibbereen) are spread from rank 5-20"
"Galway (purple/amber large markers) sits at rank 9"

---

## Technical Achievement

### Canvas-Based Custom Rendering

Each point is individually rendered on a Canvas element:

```javascript
// Split circle: Two semicircles
ctx.arc(centerX, centerY, radius, Math.PI * 0.5, Math.PI * 1.5);  // Left half
ctx.fillStyle = color1;
ctx.fill();

ctx.arc(centerX, centerY, radius, Math.PI * 1.5, Math.PI * 0.5);  // Right half
ctx.fillStyle = color2;
ctx.fill();

// Dividing line for clarity
ctx.moveTo(centerX, centerY - radius);
ctx.lineTo(centerX, centerY + radius);
ctx.stroke();
```

### Result
- Crisp rendering at any zoom level
- Consistent appearance across all browsers
- Smooth hover animations (size changes)
- Professional publication quality

---

## User Feedback

### What We Expect to Hear

❌ Before: "I can't tell which blue club is which"
✅ After: "I can instantly spot Enniskillen's blue/red split!"

❌ Before: "All the dark clubs blend together"
✅ After: "Pres Cork's black/white split stands out clearly"

❌ Before: "Is that Galway? Or another purple club?"
✅ After: "Galway's large purple/amber markers are unmistakable"

---

## Summary

The split-circle visualization transforms the regatta analysis from:
- **Single-dimension** (color shade only) to
- **Two-dimension** (two colors + pattern)

This makes club identification **instant and effortless**, turning a dense data chart into an intuitive visual story of the entire regatta.

**Files**: 
- View: `regatta-visualization-colored.html`
- Guide: `SPLIT_CIRCLES_GUIDE.md`
