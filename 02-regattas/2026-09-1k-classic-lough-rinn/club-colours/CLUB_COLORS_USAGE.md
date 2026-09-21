# Club Colors - Usage Guide

## Files Created

1. **`club_colors.md`** - Reference table of all Irish rowing clubs and their official colors
2. **`club_colors.json`** - JSON data file with club color mappings
3. **`club_color_helper.py`** - Python helper functions for easy integration

## Quick Reference

### Clubs in Your Regatta Data

| Club | Primary Color | Secondary Color | Description |
|------|---------------|-----------------|-------------|
| **Galway** | `#800080` (Purple) | `#FFBF00` (Amber) | Purple & Amber |
| **Enniskillen A/B** | `#0066CC` (Blue) | `#DC143C` (Red) | Blue & Red |
| **Methodist** | `#000080` (Navy) | `#FFFFFF` (White) | Navy Blue/White |
| **Athlone** | `#228B22` (Green) | `#DC143C` (Red) | Green & Red |
| **Castleconnel** | `#DC143C` (Red) | `#808080` (Grey) | Red & Grey |
| **Col Iognaid** | `#800000` (Maroon) | `#FFFFFF` (White) | Maroon & White |
| **Pres Cork** | `#000000` (Black) | `#FFFFFF` (White) | Black, White Hoops, Purple Trim |
| **St. Michaels** | `#4169E1` (Royal Blue) | `#CFB53B` (Old Gold) | Royal Blue & Old Gold |
| **St Josephs** | `#0066CC` (Blue) | - | Unknown (not in RI listing) |
| **Blackrock** | `#4169E1` (Royal Blue) | `#FFFFFF` (White) | Royal Blue and White |

## Python Usage

### Basic Color Lookup

```python
from club_color_helper import get_club_color, get_club_colors

# Get primary color
galway_color = get_club_color("Galway")  # Returns "#800080"

# Get all colors
galway_palette = get_club_colors("Galway")  # Returns ["#800080", "#FFBF00"]

# Get description
from club_color_helper import get_club_description
desc = get_club_description("Galway")  # Returns "Purple & Amber"
```

### Chart.js Integration

```python
from club_color_helper import create_chartjs_colors

crews = ["Galway", "Enniskillen A", "Methodist", "Athlone"]
colors = create_chartjs_colors(crews)

# Use in Chart.js dataset:
# colors['backgroundColor'] - array of colors with transparency
# colors['borderColor'] - array of solid border colors
```

### Example: Color Your Existing Data

```python
import pandas as pd
from club_color_helper import get_club_color

# Load your regatta data
df = pd.read_csv('M_J15_8x_Results.csv')

# Add color column
df['Color'] = df['Crew'].apply(get_club_color)

# Now df has a 'Color' column with hex codes for each crew
```

## JavaScript Usage

### Direct JSON Loading

```javascript
// Load the club colors
fetch('club_colors.json')
  .then(response => response.json())
  .then(data => {
    const clubColors = data.clubs;
    
    // Get Galway's primary color
    const galwayColor = clubColors['Galway'].primary;  // "#800080"
    
    // Get all Galway colors
    const galwayPalette = clubColors['Galway'].colors;  // ["#800080", "#FFBF00"]
  });
```

### Helper Function

```javascript
// Add this to your HTML visualization
function getClubColor(clubName) {
  // Assuming clubColors is loaded from club_colors.json
  const club = clubColors.clubs[clubName];
  return club ? club.primary : '#999999';  // Grey fallback
}

// Usage:
const color = getClubColor('Galway');  // "#800080"
```

## Updating Your Existing Visualization

### Current `regatta-visualization.html`

Your current visualization uses:
- Galway crews: `--galway-red: #8b0000`
- Other crews: `--maroon-bright: #5a14aa`

### To Apply Club-Specific Colors

1. **Option A: Quick Update (Chart.js data)**

In your JavaScript data section, add a `color` field:

```javascript
crews: [
    { name: "Enniskillen A", heat: "Final 1", raw: 192.9, adjusted: 201.2, color: "#0066CC" },
    { name: "Galway", heat: "Final 2", raw: 220.1, adjusted: 211.8, isGalway: true, color: "#800080" },
    // ... etc
]
```

Then use `crew.color` in your Chart.js backgroundColor/borderColor.

2. **Option B: Dynamic Lookup**

Load `club_colors.json` and create a lookup function:

```javascript
// At the top of your script section
let clubColors = {};
fetch('club_colors.json')
  .then(r => r.json())
  .then(data => {
    clubColors = data.clubs;
    // Initialize charts after colors are loaded
    initializeCharts();
  });

function getClubColor(clubName) {
  return clubColors[clubName]?.primary || '#999999';
}

// In your chart creation:
const colors = eventData.crews.map(c => getClubColor(c.name));
```

3. **Option C: Pre-process with Python**

Use the helper to generate an updated HTML file:

```python
from club_color_helper import get_club_color
import json

# Read your existing HTML
with open('regatta-visualization.html', 'r') as f:
    html = f.read()

# Create a color mapping
crew_names = ["Enniskillen A", "Galway", "Methodist", ...]  # Your crews
color_map = {name: get_club_color(name) for name in crew_names}

# Insert into HTML as a JavaScript variable
color_js = f"const CLUB_COLORS = {json.dumps(color_map)};"
# ... insert into HTML ...
```

## Notes

- **Galway Rowing Club** official colors are **Purple & Amber** (`#800080`, `#FFBF00`)
- Your current visualization uses dark red (`#8b0000`) - you may want to switch to the official purple
- All color codes are from official Rowing Ireland club listings
- Fallback color is grey (`#999999`) for unknown clubs
- Some clubs (like "St Josephs") don't appear in the Rowing Ireland listing - they use a default blue

## Future Visualizations

For any future regatta visualizations, you can:

1. Import `club_color_helper.py`
2. Apply colors automatically to all data points based on club name
3. Create consistent, recognizable color schemes across all your analyses

This ensures Galway always appears in purple/amber, Enniskillen in blue/red, etc.
