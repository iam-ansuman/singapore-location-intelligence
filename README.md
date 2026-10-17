# Singapore Location Intelligence

A decision-support tool that helps small and medium F&B businesses (cafés, restaurants, small chains) decide **which areas of Singapore to investigate first** before opening a new outlet.

It combines official Singapore open data on population, businesses, transport and geography into a ranked shortlist of subzones. Each area comes with its strengths, weaknesses and what to check next.

> **Status:** Phase 1 of 6, data audit (started 17 Oct 2026)

---

## The business question

> Using available Singapore data, which areas have characteristics that make them worth investigating for a new F&B outlet, and why?

**Who it is for:** an owner or expansion manager at a café or restaurant group with 1 to 20 outlets.

**The decision it supports:** which 5 to 10 subzones to visit, research and look for units in first.

**What a good result looks like:** a shortlist that is stable when the scoring assumptions change, with a clear reason for every area on it.

## What this tool does not do

This is a screening tool, not a guarantee of sales or profit. Public data cannot measure:

- rent or the availability of a specific unit
- actual footfall at street level
- customer spending
- whether a specific shop front will succeed

These need site visits and commercial data after the shortlist is made.

---

## Data sources

| Dataset | Source | Used for |
|---|---|---|
| Business entities (with SSIC codes) | ACRA via data.gov.sg | F&B business counts, growth over time |
| Resident population by subzone, Census 2020 | Singapore Department of Statistics via data.gov.sg | Population, density, age profile |
| MRT/LRT station exits | LTA DataMall | Transport access |
| Master Plan 2019 subzone boundaries | URA via data.gov.sg | Geographic unit for every feature |
| Postal code geocoding | OneMap API (SLA) | Turning addresses into coordinates |
| HDB resale transactions (optional) | HDB via data.gov.sg | Residential market activity |

Full details, licences and caveats are in [`data/README.md`](data/README.md).

## Method

1. **Data audit:** confirm fields, geography, dates and licence for every source
2. **Cleaning and integration:** one row per subzone, every number traceable to a source
3. **EDA and feature engineering:** densities, ratios, distances and trends
4. **Unsupervised learning:** K-means (and optionally hierarchical clustering) to find area types
5. **Location score:** a transparent weighted score, tested under different weight sets
6. **Supervised learning (only if a valid historical label exists):** logistic regression, random forest and XGBoost, with a time-based split
7. **Dashboard:** interactive Streamlit map, rankings and area profiles

Every model choice, experiment and dropped idea is recorded in [`docs/`](docs/).

## Repository structure

```
singapore-location-intelligence/
├── data/
│   ├── raw/            # downloaded files, never edited (not committed)
│   ├── processed/      # cleaned outputs from the pipeline (not committed)
│   └── external/       # small reference tables, such as SSIC code lists
├── notebooks/          # numbered in run order
├── src/                # reusable Python code used by notebooks and the dashboard
├── dashboard/          # Streamlit app
├── reports/            # business report and figures
└── docs/               # methodology, experiment log, decision log
```

## How to run

```bash
git clone https://github.com/iam-ansuman/singapore-location-intelligence.git
cd singapore-location-intelligence
python -m venv .venv
source .venv/Scripts/activate      # Git Bash on Windows
# source .venv/bin/activate        # macOS / Linux
pip install -r requirements.txt
jupyter notebook notebooks/01_data_audit.ipynb
```

Download the raw files listed in `data/README.md` into `data/raw/` before running the notebooks.

## Tech stack

Python · pandas · NumPy · GeoPandas · scikit-learn · XGBoost · Folium · Plotly · Streamlit

## Author

**Ansuman Jaiswal**, Data Science, James Cook University Singapore
GitHub: [@iam-ansuman](https://github.com/iam-ansuman)

## Licence

Code is released under the MIT Licence. Data belongs to its publishers and is used under their own terms, mostly the [Singapore Open Data Licence](https://data.gov.sg/open-data-licence).
