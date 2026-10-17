# Decision log

Every important choice, with the reason and what else was considered. This is the answer to "why did you do it that way?" in an interview.

| ID | Date | Decision | Why | Alternatives considered |
|---|---|---|---|---|
| D001 | 2026-10-17 | Target users are small and medium F&B businesses | Clear decision to support, easy to explain, also sellable as a consultancy service | Retail, clinics, gyms |
| D002 | 2026-10-17 | Geographic unit: URA Master Plan 2019 subzones | Fine enough to be useful, matches Census 2020 tables | Planning areas (too coarse), hexagon grid (harder to explain) |
| D003 | 2026-10-17 | Distances and areas calculated in SVY21 (EPSG:3414) | Metre-based, so distances are correct | Haversine on latitude/longitude |
| D004 | 2026-10-17 | Supervised models only if a credible historical label exists | Training on a score we invented proves nothing | Always include XGBoost to show more methods |
| D005 | 2026-10-17 | Standalone GitHub repo, linked from the portfolio index | Can be pinned, deployed and shown to clients on its own | Subfolder in Data-Science-portfolio- |
