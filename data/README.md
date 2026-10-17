# Data sources and audit

Raw files go in `data/raw/` and are **never edited by hand**. All cleaning happens in code. Raw and processed files are not committed to Git, so anyone rerunning the project downloads them from the links below.

Fill in the audit table as you inspect each dataset (Phase 1, task NS1-8).

## Audit table

| Dataset | File name in `data/raw/` | Downloaded on | Licence | Geography | Time span | Fields confirmed | Caveats |
|---|---|---|---|---|---|---|---|
| ACRA entities | | | | Postal code | | ☐ | Registered address may not be where customers are served |
| Census 2020 population | | | | Planning area / subzone | 2020 only | ☐ | Historical snapshot, not current population |
| LTA station exits | | | | Point coordinates | | ☐ | Check coordinate system |
| URA MP2019 subzones | | | | Polygons | 2019 boundaries | ☐ | Must match the Census subzone names |
| HDB resale (optional) | | | | Town / block | | ☐ | Not a direct measure of F&B demand |
| F&B competitor source | | | | | | ☐ | Decide which source is reliable |

## Where to find each dataset

1. **ACRA business entities.** On [data.gov.sg](https://data.gov.sg/datasets?query=ACRA), search "ACRA Information on Corporate Entities". Look for the SSIC code, registration date, entity status and postal code columns. See also the [ACRA Open Data Initiative](https://www.acra.gov.sg/resources/open-data-initiative/).
2. **Census 2020 population by subzone.** [Census 2020 dataset on data.gov.sg](https://data.gov.sg/datasets/d_9e035622439b5d25a63d7ea0699c9451/view). Look for resident counts by planning area, subzone and age group.
3. **LTA MRT/LRT station exits.** [LTA DataMall static datasets](https://datamall.lta.gov.sg/content/datamall/en/static-data.html). Download the train station exit layer.
4. **URA Master Plan 2019 subzone boundaries.** On [data.gov.sg](https://data.gov.sg/datasets?query=master+plan+2019+subzone), search "Master Plan 2019 Subzone Boundary (No Sea)" and download the GeoJSON.
5. **OneMap API.** [OneMap API docs](https://www.onemap.gov.sg/apidocs/). The search endpoint turns a postal code into coordinates. Register for a token if an endpoint needs one, and store it in a `.env` file (never in code).
6. **HDB resale prices (optional).** [HDB resale dataset on data.gov.sg](https://developers.data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view).

## Key definitions

- **F&B SSIC codes:** start with codes beginning 561 (restaurants and food service) and 563 (beverage serving). Confirm the exact codes against the SSIC 2020 list from SingStat and save the list you use to `data/external/ssic_fnb_codes.csv`.
- **Coordinate systems:** SVY21 (EPSG:3414) is in metres and is used for every distance and area calculation. WGS84 (EPSG:4326) is latitude and longitude and is used only for web maps.
- **Geographic unit:** URA Master Plan 2019 subzones (about 330), rolled up to the 55 planning areas where needed.
