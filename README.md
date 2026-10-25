# Cardiomegaly Detection

Binary classifier detecting cardiomegaly (enlarged heart) from chest scans. Built in a team within the AI MED research group at AGH.

## Approach
1. **Feature engineering** (`src/`, `feature_calc.py`) — 10 geometric features computed from heart and lung masks:
   - inertia tensor components (`xx`, `yy`, `xy`, normalized difference)
   - cardiothoracic ratio (`cr_ratio`)
   - heart width and lung width
   - custom features: `above`, `limit`, `max_dist`
2. **Model** — Random Forest (scikit-learn, 60 trees, balanced class weights), selected after comparing several models and data splits (`CSV/best_splits.ipynb`).

## Results
| Metric | Value |
|---|---|
| Cross-validation accuracy (train, 37 scans) | 0.77 ± 0.21 |
| Test accuracy (held-out, 10 scans) | 0.90 (9/10) |
| Test F1, cardiomegaly class | 0.93 |

The dataset is small (47 scans), so results should be read as a proof of concept.

## Run
```bash
pip install pandas scikit-learn scikit-image nibabel numpy jupyter
jupyter notebook main.ipynb
```
`main.ipynb` computes the features for `data/train` and `data/test`, trains the model and prints the metrics.

## Stack
Python · scikit-learn · scikit-image · nibabel · pandas · NumPy
