# Experiment log

One row per run. Log failures too: they show what you tried and why it didn't work.

**Selection rule (set before any modelling):**
- Clustering: choose k by silhouette score and elbow, but only keep it if every cluster can be described in plain words and the groups stay similar across random seeds.
- Supervised (Phase 5): compare on the validation period by PR-AUC. A model must beat logistic regression by a clear margin to justify extra complexity. The test period is used once, at the end.

| ID | Date | Phase | Model | Features | Settings | Data split | Metric(s) | Result | Notes |
|---|---|---|---|---|---|---|---|---|---|
| E001 | | CC4 | K-means | | k = 2 to 10, n_init = 20, seed 42 | all subzones | inertia, silhouette | | |
