"""Project-wide settings: paths, coordinate systems and constants.

Import from here instead of hard-coding paths in notebooks, so the project
runs the same on any machine.
"""
from pathlib import Path

# --- Paths -----------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
DATA_EXTERNAL = ROOT / "data" / "external"
REPORTS = ROOT / "reports"
FIGURES = REPORTS / "figures"

# --- Coordinate reference systems -----------------------------------------
# SVY21 is Singapore's metre-based grid. Use it for every distance and area.
CRS_SVY21 = "EPSG:3414"
# WGS84 is latitude/longitude. Use it only for web maps (Folium, Plotly).
CRS_WGS84 = "EPSG:4326"

# --- Business definitions --------------------------------------------------
# SSIC prefixes treated as F&B. Confirm against the SSIC 2020 list and
# record the final code list in data/external/ssic_fnb_codes.csv.
FNB_SSIC_PREFIXES = ("561", "563")

# --- Reproducibility -------------------------------------------------------
RANDOM_STATE = 42
