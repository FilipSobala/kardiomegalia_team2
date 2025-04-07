from skimage import measure
import numpy as np
import pandas as pd

class InertiaTensorExtractor():
    """

    Klasa służąca do obliczania tensorów bezwładności i róznicy normalizowanej dla określonych regionów (serca lub płuc) 
    w obrazach medycznych. Wyniki mogą być eksportowane do pliku CSV jako cechy do analizy.
    Różnica normalizowana jest obliczana jako (xx - yy) / (xx + yy), gdzie xx i yy to elementy tensoru bezwładności.
    Wartości różnicy normalizowanej zawsze znajdują się w przedziale [-1, 1]:
    [1] - przewaga rozszerzenia poziomego, 
    [-1] - przewaga rozszerzenia pionowego, 
    [0] - serce symetryczne

    """
    def __init__(self):
        self.feature_list = []
        
    def compute_feature_single(self, heart, value:int=2):
        """
        Oblicza tensor bezwładności(cechy: xx,yy,xy,normalized_diff) dla wybranego regionu w pojedynczym obrazie medycznym.

        :param image: Pojedyncze zdjęcie - 2D tablica numpy
        :param value: Wartość oznaczająca wybrany region:
                      - 0: Tło
                      - 1: Płuca
                      - 2: Serce (domyślna wartość - obliczanie tensorów dla serca)
        :return: słownik z wartościami tensorów bezwładności dla każdego obrazu.
                 Słownik zawiera klucze: "id","label","xx", "yy", "xy", "normalized_diff".
        :raises ValueError: Jeśli dla danego obrazu nie istnieje wybrany region (pusta maska).
        """
        image = heart.img

        mask = (image == value)

        # if np.sum(mask) == 0:
        #     raise ValueError(f"Maska dla wartości {value} jest pusta! Sprawdź dane wejściowe.")

        if np.sum(mask) == 0:
         print(f"Brak regionu {value} w obrazie {image.id}.")
         return {"id": image.id, "label": image.state, "xx": np.nan, "yy": np.nan, "xy": np.nan, "normalized_diff": np.nan}
     
        
        tensor = measure.inertia_tensor(mask)

        xx = tensor[0, 0]
        yy = tensor[1, 1]
        xy = tensor[0, 1]  # tensor[1, 0] = tensor[0, 1]

        Dx = (xx-yy)/(xx+yy)

        return {
            "id": heart.id, 
            "label": heart.state, 
            "xx": xx, 
            "yy": yy, 
            "xy": xy, 
            "normalized_diff": Dx
        }

    def compute_features(self, data, value:int=2):
        """

        Oblicza tensor bezwładności dla wybranego regionu w zbiorze obrazów medycznych.

        :param data: Lista 2D tablic numpy, reprezentujących obrazy medyczne.
        :param value: Wartość oznaczająca wybrany region:
                      - 0: Tło
                      - 1: Płuca
                      - 2: Serce (domyślna wartość - obliczanie tensorów dla serca)
        :return: Lista słowników z wartościami tensorów bezwładności dla każdego obrazu.
                 Każdy słownik zawiera klucze: "id","label","xx", "yy", "xy", "normalized_diff".
        :raises ValueError: Jeśli dla danego obrazu nie istnieje wybrany region (pusta maska).

        
        Przykład użycia:

        # Załadowanie danych
        path = r"D:\Katalog\Projects\ar_med_dane_kardio\dane_projekt_kardiomegalia\data_nifti"
        loader = DataLoader()
        loader.load_data(path)
        data = loader.get_data()

        # Obliczanie tensorów
        extractor = InertiaTensorExtractor()
        features = extractor.compute_features(data)
        print(features)

        # Zapis do CSV
        extractor.save_to_csv("tensor_features.csv")

        """
        self.feature_list = []
        
        for heart in data:
            feature = self.compute_feature_single(heart)
            self.feature_list.append(feature)

        return self.feature_list
    
    def save_to_csv(self, filename:str="tensor_features.csv"):
        """

        !!!! Koniecznie wcześniej należy wywołac metodę compute_features()!

        Zapisuje obliczone cechy tensorów bezwładności do pliku CSV.

        :param filename: Nazwa pliku do zapisania (domyślnie - 'tensor_features.csv').
        
        """
        if not self.feature_list:
            raise ValueError("Brak obliczonych cech! Upewnij się, że wywołałeś compute_features() przed zapisaniem do pliku.")
        df = pd.DataFrame(self.feature_list)
        df.to_csv(filename, index=False)

