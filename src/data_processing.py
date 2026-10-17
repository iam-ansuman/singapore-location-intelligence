"""Loading and cleaning helpers (Phase 2)."""
from __future__ import annotations

import re

import pandas as pd

from .config import FNB_SSIC_PREFIXES


def normalise_name(name: str) -> str:
    """Make area names comparable across datasets.

    The Census and URA files can spell the same subzone differently
    (case, extra spaces, punctuation). Normalise before joining on names.
    """
    if pd.isna(name):
        return ""
    name = str(name).upper().strip()
    name = re.sub(r"[^A-Z0-9 ]", " ", name)
    return re.sub(r"\s+", " ", name).strip()


def clean_postal_code(code) -> str | None:
    """Return a 6-digit Singapore postal code as text, or None if invalid.

    Postal codes must stay as strings: read as numbers, '018956' becomes 18956.
    """
    if pd.isna(code):
        return None
    digits = re.sub(r"\D", "", str(code)).split(".")[0]
    digits = digits.zfill(6)
    return digits if len(digits) == 6 else None


def is_fnb(ssic_code, prefixes: tuple[str, ...] = FNB_SSIC_PREFIXES) -> bool:
    """True if an SSIC code falls under the F&B prefixes."""
    if pd.isna(ssic_code):
        return False
    return str(ssic_code).strip().startswith(prefixes)


def report_join(left: pd.DataFrame, right: pd.DataFrame, on: str) -> pd.DataFrame:
    """Print how well two tables match on a key, and return the unmatched rows.

    Run this before every join and paste the numbers into the cleaning log.
    """
    left_keys, right_keys = set(left[on]), set(right[on])
    matched = left_keys & right_keys
    print(f"left: {len(left_keys)} keys | right: {len(right_keys)} keys | matched: {len(matched)}")
    unmatched = left[~left[on].isin(right_keys)]
    if len(unmatched):
        print(f"{len(unmatched)} left rows have no match. Check them before joining.")
    return unmatched
