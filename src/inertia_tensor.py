import numpy as np
import pandas as pd
from skimage import measure

def tensor(heart, value=2):
    image = heart.img
    mask = (image == value)

    if np.sum(mask) == 0:
        print(f"Brak regionu {value} w obrazie {heart.id}.")
        return {
            "id": heart.id,
            "label": heart.state,
            "xx": np.nan,
            "yy": np.nan,
            "xy": np.nan,
            "normalized_diff": np.nan
        }

    tensor = measure.inertia_tensor(mask)
    xx = tensor[0, 0]
    yy = tensor[1, 1]
    xy = tensor[0, 1]
    Dx = (xx - yy) / (xx + yy)

    return {
        "id": heart.id,
        "label": heart.state,
        "xx": xx,
        "yy": yy,
        "xy": xy,
        "normalized_diff": Dx
    }

