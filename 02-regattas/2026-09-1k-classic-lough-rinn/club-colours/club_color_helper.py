"""
Helper functions for applying club colors to rowing data visualizations.

Usage:
    from club_color_helper import get_club_color, get_club_colors
    
    color = get_club_color("Galway")  # Returns "#800080" (purple)
    colors = get_club_colors("Galway")  # Returns ["#800080", "#FFBF00"]
"""

import json
from pathlib import Path

# Load club colors once at module level
_COLORS_FILE = Path(__file__).parent / "club_colors.json"
with open(_COLORS_FILE, 'r') as f:
    _CLUB_DATA = json.load(f)
    CLUB_COLORS = _CLUB_DATA['clubs']


def get_club_color(club_name: str, fallback: str = "#999999") -> str:
    """
    Get the primary color for a club.
    
    Args:
        club_name: Name or abbreviation of the club (e.g., "Galway", "Galway Rowing Club")
        fallback: Color to return if club not found (default: grey)
        
    Returns:
        Hex color code (e.g., "#800080")
    """
    club = CLUB_COLORS.get(club_name)
    if club:
        return club['primary']
    return fallback


def get_club_colors(club_name: str, fallback: list = None) -> list:
    """
    Get all colors for a club.
    
    Args:
        club_name: Name or abbreviation of the club
        fallback: Colors to return if club not found (default: [grey])
        
    Returns:
        List of hex color codes (e.g., ["#800080", "#FFBF00"])
    """
    if fallback is None:
        fallback = ["#999999"]
        
    club = CLUB_COLORS.get(club_name)
    if club:
        return club['colors']
    return fallback


def get_club_description(club_name: str) -> str:
    """
    Get the color description for a club.
    
    Args:
        club_name: Name or abbreviation of the club
        
    Returns:
        Color description (e.g., "Purple & Amber")
    """
    club = CLUB_COLORS.get(club_name)
    if club:
        return club['description']
    return "Unknown"


def list_clubs() -> list:
    """
    Get a list of all club names in the database.
    
    Returns:
        List of club names
    """
    return list(CLUB_COLORS.keys())


# Create a color mapping for Chart.js datasets
def create_chartjs_colors(crew_names: list) -> dict:
    """
    Create Chart.js compatible color arrays for a list of crews.
    
    Args:
        crew_names: List of crew/club names
        
    Returns:
        Dict with 'backgroundColor' and 'borderColor' arrays
    """
    bg_colors = []
    border_colors = []
    
    for name in crew_names:
        primary = get_club_color(name)
        bg_colors.append(primary + "CC")  # Add alpha for slight transparency
        border_colors.append(primary)
    
    return {
        'backgroundColor': bg_colors,
        'borderColor': border_colors
    }


# Example usage
if __name__ == "__main__":
    print("=== Club Color Helper Demo ===\n")
    
    # Demo clubs from your regatta
    demo_clubs = [
        "Galway", "Athlone", "Enniskillen A", "Methodist", 
        "Castleconnel", "Col Iognaid", "Pres Cork", "St. Michaels"
    ]
    
    print("Primary colors:")
    for club in demo_clubs:
        color = get_club_color(club)
        desc = get_club_description(club)
        print(f"  {club:20} -> {color:8} ({desc})")
    
    print("\nFull color palettes:")
    for club in ["Galway", "Enniskillen A", "Methodist"]:
        colors = get_club_colors(club)
        print(f"  {club:20} -> {colors}")
    
    print("\nChart.js color mapping:")
    chart_colors = create_chartjs_colors(demo_clubs[:4])
    print(f"  Background: {chart_colors['backgroundColor'][:2]}...")
    print(f"  Border:     {chart_colors['borderColor'][:2]}...")
