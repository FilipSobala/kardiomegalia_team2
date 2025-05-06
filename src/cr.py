import numpy as np 
from skimage import measure


def cr_ratio(heart):
    img = heart.img  
    mask = img == 2
    area_heart = np.sum(mask)

    if area_heart == 0:
        print(f"Brak serca w obrazie {heart.id}!")
        return {"id": heart.id, "stosunek": None}

    binary_image = (img == 2).astype(int)
    circuit = measure.perimeter(binary_image)

    ratio = area_heart / circuit if circuit > 0 else None

    return {"id": heart.id, "label": heart.is_cardiomegalia(), "cr_ratio": ratio}
