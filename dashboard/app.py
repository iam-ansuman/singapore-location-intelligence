"""Streamlit dashboard (Phase 6).

Run locally with:  streamlit run dashboard/app.py
"""
import streamlit as st

st.set_page_config(page_title="Singapore Location Intelligence", layout="wide")

st.title("Singapore Location Intelligence")
st.caption("Screening Singapore subzones for new F&B outlets")

st.info(
    "The dashboard is built in Phase 6. It will show a map of subzone scores, "
    "a ranked shortlist, filters by planning area and cluster, and a profile "
    "for each area with its strengths, weaknesses and caveats."
)
