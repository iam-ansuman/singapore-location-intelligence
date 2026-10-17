# Decision log

Every important choice, with the reason and what else was considered. This is the answer to "why did you do it that way?" in an interview.

| ID | Date | Decision | Why | Alternatives considered |
|---|---|---|---|---|
| D001 | 2026-10-17 | Target users are small and medium F&B businesses | Clear decision to support, easy to explain, also sellable as a consultancy service | Retail, clinics, gyms |
| D002 | 2026-10-17 | Geographic unit: URA Master Plan 2019 subzones | Fine enough to be useful, matches Census 2020 tables | Planning areas (too coarse), hexagon grid (harder to explain) |
| D003 | 2026-10-17 | Distances and areas calculated in SVY21 (EPSG:3414) | Metre-based, so distances are correct | Haversine on latitude/longitude |
| D004 | 2026-10-17 | Supervised models only if a credible historical label exists | Training on a score we invented proves nothing | Always include XGBoost to show more methods |
| D005 | 2026-10-17 | Standalone GitHub repo, linked from the portfolio index | Can be pinned, deployed and shown to clients on its own | Subfolder in Data-Science-portfolio- |
| D006 | 2026-10-17 | Use the newest version of every dataset, except keep MP2019 subzone boundaries | Current data makes the shortlist relevant. MP2019 boundaries are kept because the SingStat population tables use the same subzones, so names join cleanly | Draft Master Plan 2025 boundaries (subzones may not match population data) |
| D007 | 2026-10-17 | Population from SingStat June 2025 instead of Census 2020, plus 2021 to 2024 for trends | Newer, and the yearly series allows growth features and possibly a real historical label | Census 2020 only (a single old snapshot) |
| D008 | 2026-10-17 | Add NEA hawker centres as a competitor layer | Hawker stalls are a major low-cost alternative and are not captured as ACRA companies | Ignore hawkers |
| D009 | 2026-10-17 | Add LTA passenger volume (train stations and bus stops) as the footfall signal | Residents miss office workers, students and shoppers. Tap-outs are the best free proxy for daytime demand | Residents only; paid mobile location data |
| D010 | 2026-10-17 | Add OpenStreetMap points of interest for competitors and attractors | Real coordinates and categories (café vs restaurant vs fast food); ACRA only shows registered companies | Google Places (paid, restrictive terms) |
| D011 | 2026-10-17 | Use GHS 2025 household income by planning area, falling back to Census 2020 | Spending power decides whether premium pricing works | Ignore income |
| D012 | 2026-10-17 | Organise features into four pillars: demand, access, spending power, supply | Makes the score explainable to a business owner and keeps feature selection disciplined | Unstructured feature list |
| D013 | 2026-10-17 | Final dataset list locked; later changes need a decision-log entry | Stops scope creep and keeps the audit trail clean | Keep adding sources ad hoc |
