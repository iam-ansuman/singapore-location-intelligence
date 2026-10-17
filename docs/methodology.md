# Methodology

This document grows as the project goes. By the end it becomes the methods section of the business report.

## 1. Problem definition
Which Singapore subzones are worth investigating first for a new F&B outlet, and why? See the README for scope and limits.

## 2. Data
_Summarise from `data/README.md` once the audit is complete: sources, dates, licences, geography and caveats._

## 3. Cleaning and integration
_Rows in and out at each step, how names and postal codes were matched, and what was dropped._

## 4. Features
_The feature dictionary: name, formula, unit, source, and whether higher is better or worse._

## 5. Unsupervised learning
_K-means: features used, scaling, k chosen and why, cluster profiles. Hierarchical clustering: whether it agreed with K-means._

## 6. Location score
_Indicators, weights, directions, missing-value handling, and the sensitivity test across weight sets._

## 7. Supervised learning (if applicable)
_The label and how it was defined, the time-based split, models compared, metrics, explanation of predictions, leakage checks. If no valid label existed, explain why this step was skipped._

## 8. Model comparison

| Model | Validation score | Training time | Interpretability | Chosen? | Reason |
|---|---|---|---|---|---|
| | | | | | |

## 9. What didn't work
_Features, models and ideas that were tried and dropped, with the reason._

## 10. Limitations and next steps
_What the tool cannot tell a business, and what data would improve it._
