# Data sources and audit

**Final dataset list, locked 17 Oct 2026.** Changes after this date go in `docs/decision_log.md` with a reason.

Raw files go in `data/raw/` and are **never edited by hand**. All cleaning happens in code. Raw and processed files are not committed to Git, so anyone rerunning the project downloads them from the sources below.

**Rules for data in this project**
1. Use the newest available version of every dataset, and record its "last updated" date and your download date.
2. The one deliberate exception is the boundary file: MP2019 subzones, because the SingStat population tables use the same subzones (D006).
3. Every feature in the model must trace back to a row in this file.

## How the data answers the business question

A café or restaurant does well where there are **enough people nearby (demand)**, who can **reach it easily (access)**, who **can afford it (spending power)**, and where **competition is not already saturated (supply)**. Each dataset below feeds one of these four pillars.

## Final dataset list

### A. Geography (the unit of analysis)

| ID | Dataset | Publisher | Version | Format | Used for |
|---|---|---|---|---|---|
| G1 | Master Plan 2019 Subzone Boundary (No Sea) | URA via data.gov.sg | MP2019 | GeoJSON | One row per subzone; area in km²; all spatial joins |

### B. Demand (who is nearby)

| ID | Dataset | Publisher | Version | Format | Features |
|---|---|---|---|---|---|
| D1 | Singapore Residents by Planning Area / Subzone, Age Group, Sex and Type of Dwelling | SingStat | **June 2025** (confirmed) | CSV | Residents, density per km², share aged 20 to 39, share in condos vs HDB |
| D2 | Same table, earlier years | SingStat | June 2021 to 2024; 2011 to 2020 | CSV | 5-year and 10-year population growth; historical label for Phase 5 |
| D3 | Passenger Volume by Train Stations | LTA DataMall | Latest months; save every month from now on | CSV (via API) | Weekday lunchtime (11 to 14h) tap-outs, evening tap-outs, weekend volume per station |
| D4 | Passenger Volume by Bus Stops | LTA DataMall | Latest months; save every month | CSV (via API) | Same footfall measures at bus-stop level, aggregated to subzones |

### C. Access (how easily people reach it)

| ID | Dataset | Publisher | Version | Format | Features |
|---|---|---|---|---|---|
| A1 | LTA MRT Station Exit | LTA via data.gov.sg | Latest | GeoJSON | Distance from subzone to nearest exit; exits per subzone |
| A2 | Bus Stops | LTA DataMall | Latest | JSON (via API) | Bus stop coordinates (needed to place D4 on the map); stops per km² |

### D. Spending power

| ID | Dataset | Publisher | Version | Format | Features |
|---|---|---|---|---|---|
| S1 | General Household Survey 2025 | SingStat | Published 30 Jun 2026 | Excel / CSV | Household income by planning area, **if** a planning-area table exists |
| S1b | Census of Population 2020 (fallback) | SingStat | 2020 | Excel / CSV | Household income by planning area, only if S1 has no planning-area table |
| S2 | HDB Resale Flat Prices (Jan 2017 onwards) | HDB via data.gov.sg | Latest | CSV | Median price per m² by town, as an affordability signal |

### E. Supply and competition (who is already there)

| ID | Dataset | Publisher | Version | Format | Features |
|---|---|---|---|---|---|
| C1 | ACRA Information on Corporate Entities | ACRA via data.gov.sg | Latest monthly release | CSV (may be several files) | Live F&B entities (SSIC 561xx, 563xx) per subzone; new registrations per year |
| C2 | OpenStreetMap points of interest | OpenStreetMap contributors | Extract date recorded | GeoJSON (via Overpass API) | Cafés, restaurants, fast food and food courts per subzone and per 1,000 people |
| C3 | Hawker Centres | NEA via data.gov.sg | Latest | GeoJSON | Hawker centres within 500 m; low-cost competition |
| C4 | SFA licensed food establishments | SFA via data.gov.sg | Check | CSV | Cross-check for C1 and C2, **if** a full list with addresses is published |

### F. Attractors (places that pull people in)

| ID | Dataset | Publisher | Version | Format | Features |
|---|---|---|---|---|---|
| F1 | OpenStreetMap: malls, offices, schools, universities, parks | OpenStreetMap contributors | Same extract as C2 | GeoJSON | Count of attractors per subzone; distance to nearest mall |
| F2 | HDB Property Information | HDB via data.gov.sg | Latest | CSV | HDB blocks with commercial units (neighbourhood centres) |

### Tools (not datasets)

| ID | Tool | Publisher | Used for |
|---|---|---|---|
| T1 | OneMap Search API | SLA | Turning ACRA postal codes into coordinates. Cache every result |
| T2 | LTA DataMall API key | LTA | Required for D3, D4 and A2. Free sign-up. Keep it in `.env` |

## Considered and not used

| Dataset | Why not |
|---|---|
| Census 2020 population | Replaced by SingStat June 2025 (D007) |
| Draft Master Plan 2025 boundaries | Subzones may not match the SingStat population tables (D006) |
| Google Places API | Paid, and its terms limit storing and redistributing results |
| URA REALIS rents | Paid subscription. Rent stays a stated limitation |
| Mobile location or card spending data | Not publicly available |

## Where to get them

- **SingStat (D1, D2):** [Geographic distribution page](https://www.singstat.gov.sg/find-data/search-by-theme/population/geographic-distribution). Click the CSV icon next to each year.
- **SingStat GHS 2025 (S1):** [General Household Survey 2025](https://www.singstat.gov.sg/publication-resources/general-household-survey-2025). Check the statistical tables list for anything "by planning area".
- **data.gov.sg (G1, A1, S2, C1, C3, C4, F2):** search each name on [data.gov.sg](https://data.gov.sg). For example [MP2019 subzones](https://data.gov.sg/dataset/master-plan-2019-subzone-boundary-no-sea), [MRT exits](https://data.gov.sg/dataset/lta-mrt-station-exit), [hawker centres](https://data.gov.sg/dataset/hawker-centres). Copy the "Last updated" date into the audit table.
- **LTA DataMall (D3, D4, A2):** sign up for a free API key at [LTA DataMall](https://datamall.lta.gov.sg/content/datamall/en/static-data.html). Passenger volume calls return a link to a monthly CSV.
- **OpenStreetMap (C2, F1):** query Singapore with the [Overpass API](https://overpass-api.de/) from a notebook. Credit "© OpenStreetMap contributors" in the dashboard and report.
- **ACRA (C1):** see also the [ACRA Open Data Initiative](https://www.acra.gov.sg/resources/open-data-initiative/).

## Download order

| Day | Datasets | Why this order |
|---|---|---|
| 1 | G1, D1, A1, C3 | Small files. Enough to make the first map and test the name join |
| 2 | Sign up for T2. D3, D4, A2 | Footfall is the most important new signal |
| 3 | C1 | Large. Needs filtering and geocoding with T1 |
| 4 | C2, F1 (one Overpass query) | Competitor and attractor layers |
| 5 | D2, S1 / S1b, S2, F2, C4 | Trends, income and the remaining context |

## Audit table

Fill this in as you inspect each dataset (Phase 1, task NS1-8).

| ID | File name in `data/raw/` | Last updated (source) | Downloaded on | Licence | Geography | Time span | Fields confirmed | Caveats |
|---|---|---|---|---|---|---|---|---|
| G1 | | MP2019 | | SG Open Data Licence | Subzone polygons | 2019 | ☐ | Must match SingStat names |
| D1 | | June 2025 | | SingStat terms | Subzone | June 2025 | ☐ | Residents only (citizens and PRs) |
| D2 | | | | SingStat terms | Subzone | 2011 to 2024 | ☐ | Check subzone names are consistent across years |
| D3 | | | | DataMall terms | Station | Monthly | ☐ | Only recent months available; save monthly |
| D4 | | | | DataMall terms | Bus stop | Monthly | ☐ | Large file |
| A1 | | | | SG Open Data Licence | Points | | ☐ | Check CRS |
| A2 | | | | DataMall terms | Points | | ☐ | API returns 500 rows per call; page through |
| S1 | | 30 Jun 2026 | | SingStat terms | Planning area? | 2025 | ☐ | Confirm planning-area table exists |
| S2 | | | | SG Open Data Licence | Town / block | 2017 onwards | ☐ | Town level, coarser than subzone |
| C1 | | | | SG Open Data Licence | Postal code | | ☐ | Registered address may not be the outlet |
| C2 | | | | ODbL | Points | Extract date | ☐ | Volunteer data; coverage varies |
| C3 | | | | SG Open Data Licence | Points | | ☐ | |
| C4 | | | | SG Open Data Licence | | | ☐ | May not exist as a full list |
| F1 | | | | ODbL | Points / polygons | Extract date | ☐ | |
| F2 | | | | SG Open Data Licence | Block | | ☐ | |

## Key definitions

- **F&B SSIC codes:** codes beginning 561 (restaurants and food service) and 563 (beverage serving). Confirm the exact codes against the SSIC 2020 list from SingStat and save the list you use to `data/external/ssic_fnb_codes.csv`.
- **Residents:** SingStat counts citizens and permanent residents only. Workers on passes, tourists and commuters are missing, which is why D3 and D4 matter.
- **Lunchtime footfall:** weekday tap-outs between 11:00 and 14:00, the core trading window for most F&B outlets.
- **Coordinate systems:** SVY21 (EPSG:3414) is in metres and is used for every distance and area calculation. WGS84 (EPSG:4326) is latitude and longitude and is used only for web maps.
- **Geographic unit:** URA Master Plan 2019 subzones, rolled up to the 55 planning areas where needed.
