# Club Color Coding System

Official color mapping for Irish rowing clubs based on Rowing Ireland's club listings.

## 📁 Files Created

### Core Data Files
- **`club_colors.json`** (16KB) - Complete database of 75+ clubs with hex color codes
- **`club_colors.md`** (7.5KB) - Human-readable reference table
- **`club_color_helper.py`** (3.5KB) - Python utility functions
- **`CLUB_COLORS_USAGE.md`** (5.4KB) - Detailed integration guide

### Visualization Files
- **`regatta-visualization-colored.html`** - Updated visualization with official club colors
- **`regatta-visualization.html.backup`** - Backup of original
- **`update_visualization_colors.py`** - Script used to apply colors

## 🎨 Key Color Changes

### Galway Rowing Club
- **Old**: `#8b0000` (dark red)
- **New**: `#800080` (official purple)
- **Secondary**: `#FFBF00` (amber)
- **Source**: Official Rowing Ireland listing

### Other Clubs in Your Regatta

| Club | Primary Color | Description |
|------|---------------|-------------|
| Enniskillen A/B | `#0066CC` | Blue & Red |
| Methodist | `#000080` | Navy Blue/White |
| Athlone | `#228B22` | Green & Red |
| Castleconnel | `#DC143C` | Red & Grey |
| Col Iognaid | `#800000` | Maroon & White |
| Pres Cork | `#000000` | Black, White Hoops, Purple Trim |
| St. Michaels | `#4169E1` | Royal Blue & Old Gold |
| Blackrock | `#4169E1` | Royal Blue and White |

## 🚀 Quick Start

### Python

```python
from club_color_helper import get_club_color

# Get a club's color
color = get_club_color("Galway")  # Returns "#800080"

# Apply to your data
import pandas as pd
df = pd.read_csv('M_J15_8x_Results.csv')
df['Color'] = df['Crew'].apply(get_club_color)
```

### JavaScript (in HTML)

The updated `regatta-visualization-colored.html` now includes:

```javascript
// Access club colors
const galwayColor = getClubColor("Galway");  // "#800080"

// Use in Chart.js
backgroundColor: eventData.crews.map(c => getClubColor(c.name))
```

## 📊 Data Coverage

- **Total clubs**: 75+
- **Clubs in your regatta**: 13 (all mapped)
- **Source**: https://www.rowingireland.ie/rowing-for-all/find-a-club-in-your-area/
- **Updated**: September 21, 2026

## 🔧 Integration Examples

### 1. Color a scatter plot

```python
import matplotlib.pyplot as plt
from club_color_helper import get_club_color

crews = ["Galway", "Enniskillen A", "Methodist"]
times = [220.1, 192.9, 200.0]
colors = [get_club_color(c) for c in crews]

plt.scatter(range(len(crews)), times, c=colors, s=100)
plt.xticks(range(len(crews)), crews)
plt.ylabel('Time (s)')
plt.show()
```

### 2. Generate Chart.js colors

```python
from club_color_helper import create_chartjs_colors

crews = ["Galway A", "Galway B", "Athlone", "Methodist"]
colors = create_chartjs_colors(crews)

# colors['backgroundColor'] has semi-transparent fills
# colors['borderColor'] has solid borders
```

### 3. Build a legend

```python
from club_color_helper import get_club_description, get_club_color

for club in ["Galway", "Enniskillen A", "Methodist"]:
    color = get_club_color(club)
    desc = get_club_description(club)
    print(f"● {club}: {desc} ({color})")
```

Output:
```
● Galway: Purple & Amber (#800080)
● Enniskillen A: Blue & Red (#0066CC)
● Methodist: Navy Blue/White (#000080)
```

## 📝 Notes

1. **Galway colors** are now the official Purple & Amber, not the previous dark red
2. **All clubs** from your regatta data are included with official colors
3. **Fallback color** is grey (`#999999`) for unknown clubs
4. **Name variations** are handled (e.g., "Galway", "Galway A", "Galway Rowing Club" all work)
5. Colors are sourced from **official Rowing Ireland listings** as of September 2026

## 🔮 Future Use

For any new regatta analysis:

1. Import the color helper
2. Apply colors based on club names
3. Your visualizations will automatically use consistent, official club colors

This ensures:
- ✅ Consistent branding across all visualizations
- ✅ Easy club identification at a glance
- ✅ Professional appearance using official colors
- ✅ Automatic color assignment for new data

## 📖 See Also

- **CLUB_COLORS_USAGE.md** - Detailed usage guide with more examples
- **club_colors.md** - Full reference table of all clubs
- **club_color_helper.py** - Source code with all utility functions

---

**Generated**: September 21, 2026  
**Source**: Rowing Ireland official club listings
