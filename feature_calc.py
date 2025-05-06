"""
tensor xx yy xy normalize_diff
limit above 90 max_dist

circled ratio
lungs_width heart_width



"""
from src.manage import DataLoader
from src.above import above
from src.cr import cr_ratio
from src.inertia_tensor import tensor
from src.width import f_get_longest_width
import os
import pandas as pd

DEBUG = False
BASE_DIR = R"\."


def calculate_features(data_path,label_path, filename):
    if DEBUG:
        print("Data dir exists?", os.path.exists(data_path))
        print("Label file exists?", os.path.exists(label_path))

    loader = DataLoader()
    loader.load_data(data_path, label_path)
    data = loader.get_data()

    # print("Data dir exists?", os.path.exists(data_path))
    # print("Label file exists?", os.path.exists(label_path))

    file_path = os.path.join(BASE_DIR, filename)
    data_for_csv = []
    for heart in data:
        above_features = above(heart)
        cr_ratio_features = cr_ratio(heart)
        tensor_features = tensor(heart)
        width_features = f_get_longest_width(heart)

        combined_features = {
            **above_features,
            **cr_ratio_features,
            **tensor_features,
            **width_features
        }

        data_for_csv.append(combined_features)

    df = pd.DataFrame(data_for_csv)
    df.to_csv(file_path, index=False)

    print("Processing finished")
