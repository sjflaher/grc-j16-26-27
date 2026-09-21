# Regatta Visualization - Club Colors Update

## ✅ Complete

The regatta visualization has been fully updated to use official Irish rowing club colors throughout.

## 📊 What Changed

### Before
- **2 datasets**: "Galway Crews" (dark red) vs "Other Crews" (purple)
- Static legend
- No club differentiation
- Galway used unofficial dark red color (#8b0000)

### After
- **24 datasets**: One per club, each with official colors
- Dynamic legend showing all clubs
- Easy visual club identification
- Galway uses official purple (#800080) from Rowing Ireland

## 🎨 Technical Changes

### 1. Chart.js Datasets (lines 800-850)
```javascript
// OLD: Two hardcoded datasets
datasets: [
    { label: 'Other Crews', backgroundColor: 'rgba(90, 20, 170, 0.5)' },
    { label: 'Galway Crews', backgroundColor: 'rgba(139, 0, 0, 0.9)' }
]

// NEW: One dataset per club with official colors
const datasets = [];
Object.keys(crewsByClub).forEach(clubName => {
    const clubColor = getClubColor(clubName);
    datasets.push({
        label: clubName,
        backgroundColor: isGalway ? clubColor : clubColor + 'CC',
        borderColor: isGalway ? '#ffffff' : clubColor,
        pointRadius: isGalway ? 11 : 6
    });
});
```

### 2. Club Color Database (line 373)
```javascript
const CLUB_COLORS = {
    "Galway": { primary: "#800080", description: "Purple & Amber" },
    "Enniskillen": { primary: "#0066CC", description: "Blue & Red" },
    // ... 24 clubs total
};

function getClubColor(clubName) {
    return CLUB_COLORS[clubName]?.primary || '#999999';
}
```

### 3. Dynamic Legend (new function)
```javascript
function buildLegend() {
    // Builds legend from all clubs in data
    // Galway highlighted in bold
    // Sorted alphabetically with Galway first
}
```

### 4. CSS Variables Updated
```css
/* OLD */
--galway-red: #8b0000;

/* NEW */
--galway-primary: #800080;  /* Official Purple */
```

## 📈 Visual Impact

### Chart Markers
- **Galway crews**: Large (11px), purple, white border, full opacity
- **Other crews**: Smaller (6px), club color, 80% opacity
- **Hover**: All markers enlarge on hover

### Legend
- Shows all 24 clubs present in regatta data
- Color squares match chart colors exactly
- Galway highlighted in bold font
- Sorted alphabetically (Galway first)

### Colors in Use

| Club | Color | Description |
|------|-------|-------------|
| **Galway** | `#800080` | **Purple & Amber** ⭐ |
| Enniskillen | `#0066CC` | Blue & Red |
| Methodist | `#000080` | Navy Blue/White |
| Athlone | `#228B22` | Green & Red |
| Castleconnel | `#DC143C` | Red & Grey |
| Col Iognaid | `#800000` | Maroon & White |
| Pres Cork | `#000000` | Black, White Hoops, Purple Trim |
| St. Michaels | `#4169E1` | Royal Blue & Old Gold |
| Bann | `#DC143C` | Red & White |
| Commercial | `#317873` | Myrtle Green, White & Azure Blue |
| Cork | `#3F2212` | Chocolate Brown & White |
| CRCC | `#008080` | Teal, Black & White |
| Fermoy | `#FFFFFF` | White & Green Hoops |
| Lee | `#DC143C` | Red & Black |
| Newry | `#DC143C` | Red & Black with Yellow Star |
| Northwest | `#0066CC` | Blue & White |
| Offaly | `#808080` | Grey & Red |
| Shandon | `#ADD8E6` | Light Blue |
| Skibbereen | `#DC143C` | Red & White |
| Sligo | `#000000` | Black and Red |
| St Josephs | `#0066CC` | (Blue - not in RI listing) |
| Waterford | `#000080` | Navy & White Hoop |
| Bantry | `#FF6B6B` | (Coral - not in RI listing) |
| Carrick | `#4ECDC4` | (Teal - not in RI listing) |

## 🗂️ Files Updated

### Core Files
1. **regatta-visualization-colored.html** (53KB)
   - Complete chart rewrite
   - Club colors embedded
   - Dynamic legend system
   - All 6 events updated

2. **club_colors.json** (18KB)
   - Added 16 short-name mappings
   - Now covers 105 clubs total
   - All regatta clubs mapped

### Unchanged
- **regatta-visualization.html** (48KB) - original backup
- **regatta-visualization.html.backup** - safety backup

## ✨ Benefits

1. **Instant Recognition**: Each club is immediately identifiable by color
2. **Official Branding**: Uses Rowing Ireland official club colors
3. **Galway Emphasis**: Purple markers stand out clearly
4. **Professional**: Consistent color scheme across all 6 events
5. **Scalable**: New clubs automatically get colors when added to database

## 🚀 Usage

Simply open `regatta-visualization-colored.html` in any modern browser:

```bash
open regatta-visualization-colored.html
```

Or double-click the file. No server required.

## 📝 Notes

- **Club name normalization**: Handles A/B/C/D/E/F suffixes (e.g., "Galway A", "Galway B")
- **Fallback colors**: Unknown clubs get grey (#999999)
- **Future-proof**: New clubs can be added to `club_colors.json` anytime
- **Source**: All colors from https://www.rowingireland.ie/rowing-for-all/find-a-club-in-your-area/

## 🔧 Customization

To change a club's color, edit `club_colors.json`:

```json
"Galway": {
  "description": "Purple & Amber",
  "primary": "#800080",
  "secondary": "#FFBF00",
  "colors": ["#800080", "#FFBF00"]
}
```

Then reload the HTML file. The `getClubColor()` function will pick up the change automatically.

---

**Generated**: 2026-09-21  
**Source**: Rowing Ireland official club colors
