"""Transparent location score and sensitivity testing (Phase 4)."""
from __future__ import annotations

import pandas as pd


def zscore(s: pd.Series) -> pd.Series:
    """Standardise one indicator."""
    return (s - s.mean()) / s.std(ddof=0)


def location_score(df: pd.DataFrame, weights: dict[str, float],
                   direction: dict[str, int]) -> pd.Series:
    """Score = sum(weight x standardised indicator), rescaled to 0-100.

    weights:   {"pop_density": 0.3, ...}  should sum to 1
    direction: {"pop_density": +1, "nearest_mrt_m": -1, ...}
               +1 if higher is better, -1 if higher is worse
    """
    raw = sum(w * direction[c] * zscore(df[c]) for c, w in weights.items())
    return 100 * (raw - raw.min()) / (raw.max() - raw.min())


def ranking_stability(df: pd.DataFrame, weight_sets: dict[str, dict],
                      direction: dict[str, int], top_n: int = 10) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Compare rankings under several weight sets.

    Returns (Spearman correlation between rankings, top-N areas for each set).
    High correlations and a shared top 10 mean the shortlist is robust.
    """
    scores = pd.DataFrame({name: location_score(df, w, direction) for name, w in weight_sets.items()})
    corr = scores.rank(ascending=False).corr(method="spearman")
    tops = pd.DataFrame({name: scores[name].nlargest(top_n).index.tolist() for name in scores})
    return corr, tops
