# Opisy cech w poszczególnych plikach

---

### longest_width.csv
- lungs_width - najdłuższa szerokość płuc
- heart_width - najdłuższa szerokość serca

---
### maps
- first idea - pixel distribution, basicly maps histogram to five values


### center_of_mass.py
-  heart's center of mass -> tuple(y : int, x : int)

### polygon_area_ratio.py
- heart's best fitted polygon area to lung's best fitted polygon area ratio

### inertia_tensor.py / tensor_features.csv

Computes the inertia tensor of the heart (or lungs, if provided) and its normalized difference.

Features:  
`id`, `label`, `xx`, `yy`, `xy`, `normalized_diff`

The class in `inertia_tensor.py` returns:  
- CSV columns (if exporting to CSV via `save_to_csv`)  
- A list of dictionaries (if using `compute_features`)  
- A single dictionary (if using `compute_feature_single`)


