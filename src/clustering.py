"""Unsupervised learning: K-means model selection (Phase 4)."""
from __future__ import annotations

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

from .config import RANDOM_STATE


def scale_features(X: pd.DataFrame) -> tuple[pd.DataFrame, StandardScaler]:
    """Standardise features to mean 0, standard deviation 1.

    K-means uses distances, so unscaled population (tens of thousands)
    would drown out MRT distance (hundreds of metres).
    """
    scaler = StandardScaler()
    Xs = pd.DataFrame(scaler.fit_transform(X), index=X.index, columns=X.columns)
    return Xs, scaler


def evaluate_k_range(Xs: pd.DataFrame, k_values=range(2, 11)) -> pd.DataFrame:
    """Fit K-means for each k and return inertia and silhouette score.

    Plot both columns: look for the elbow in inertia and a high silhouette.
    Record the result as a row in docs/experiment_log.md.
    """
    rows = []
    for k in k_values:
        km = KMeans(n_clusters=k, n_init=20, random_state=RANDOM_STATE).fit(Xs)
        rows.append({"k": k, "inertia": km.inertia_,
                     "silhouette": silhouette_score(Xs, km.labels_)})
    return pd.DataFrame(rows)


def profile_clusters(X_original: pd.DataFrame, labels) -> pd.DataFrame:
    """Median of each feature per cluster, in original units, for interpretation."""
    out = X_original.copy()
    out["cluster"] = labels
    summary = out.groupby("cluster").median()
    summary["n_areas"] = out.groupby("cluster").size()
    return summary
