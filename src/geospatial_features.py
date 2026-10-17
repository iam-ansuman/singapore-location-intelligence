"""Geospatial features: spatial joins, densities and distances (Phases 2 and 3)."""
from __future__ import annotations

import geopandas as gpd
import pandas as pd

from .config import CRS_SVY21


def to_svy21(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Reproject to SVY21 metres. Always do this before distance or area maths."""
    if gdf.crs is None:
        raise ValueError("Layer has no CRS. Set it with .set_crs() before converting.")
    return gdf.to_crs(CRS_SVY21)


def points_from_latlon(df: pd.DataFrame, lat: str = "latitude", lon: str = "longitude") -> gpd.GeoDataFrame:
    """Turn a table with latitude/longitude columns into a point layer."""
    return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[lon], df[lat]), crs="EPSG:4326")


def count_points_in_polygons(points: gpd.GeoDataFrame, polygons: gpd.GeoDataFrame,
                             area_id: str, name: str = "count") -> pd.Series:
    """Count how many points fall inside each polygon (point-in-polygon join)."""
    points, polygons = to_svy21(points), to_svy21(polygons)
    joined = gpd.sjoin(points, polygons[[area_id, "geometry"]], how="inner", predicate="within")
    counts = joined.groupby(area_id).size().rename(name)
    return counts.reindex(polygons[area_id], fill_value=0)


def area_km2(polygons: gpd.GeoDataFrame, area_id: str) -> pd.Series:
    """Polygon area in square kilometres."""
    p = to_svy21(polygons)
    return pd.Series(p.geometry.area.values / 1e6, index=p[area_id], name="area_km2")


def nearest_distance_m(polygons: gpd.GeoDataFrame, points: gpd.GeoDataFrame,
                       area_id: str, name: str = "nearest_m") -> pd.Series:
    """Distance in metres from each polygon's centroid to the nearest point.

    Example: distance from each subzone to its nearest MRT exit.
    """
    p = to_svy21(polygons)[[area_id, "geometry"]].copy()
    p["geometry"] = p.geometry.centroid
    pts = to_svy21(points)[["geometry"]]
    joined = gpd.sjoin_nearest(p, pts, how="left", distance_col=name)
    return joined.groupby(area_id)[name].min()
