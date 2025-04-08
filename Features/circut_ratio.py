import numpy as np
import pandas as pd
from skimage import measure


class CircutRatioExtractor:
    def __init__(self):
        self.feature_list = []

    def compute_single_circut(self, image):
        heart = image.img
        mask = (heart == 2)
        area_heart = np.sum(mask)

        if area_heart == 0:
            print(f"Brak serca w obrazie {image.id}!")
            return {"id": image.id, "stosunek": None}

        binary_image = (heart == 2).astype(int)
        circuit = measure.perimeter(binary_image)

        ratio = area_heart / circuit if circuit > 0 else None

        return {
            "id": image.id,
            "label": image.state,
            "circut_ratio": ratio
        }

    def compute_circut(self, data):
        self.feature_list = []
        for image in data:
            feature = self.compute_single_circut(image)
            self.feature_list.append(feature)
        return self.feature_list

    def save_to_csv(self, filename="cr_features.csv"):
        if self.feature_list:
            df = pd.DataFrame(self.feature_list)
            df.to_csv(filename, index=False)