import numpy as np
import pandas as pd

class AreaRatioExtractor:
    def __init__(self):
        self.feature_list = []

    def compute_single_circut(self, image):
        pic = image.img
        mask_heart = (pic == 2)
        area_heart = np.sum(mask_heart)
        mask_lung = (pic == 1)
        area_lung = np.sum(mask_lung)

        if area_heart == 0 or area_lung==0:
            print(f"Brak serca w obrazie {image.id}!")
            return {"id": image.id, "stosunek": None}

        ratio = area_heart / area_lung if area_lung > 0 else None

        return {
            "id": image.id,
            "label": image.state,
            "area_ratio": ratio
        }

    def compute_circut(self, data):
        self.feature_list = []
        for image in data:
            feature = self.compute_single_circut(image)
            self.feature_list.append(feature)
        return self.feature_list

    def save_to_csv(self, filename="ar_features.csv"):
        if self.feature_list:
            df = pd.DataFrame(self.feature_list)
            df.to_csv(filename, index=False)