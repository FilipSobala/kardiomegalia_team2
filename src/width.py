from skimage import measure
from src.heart import Heart


def f_get_longest_width(heart):
    img = heart.get_img()
    label = measure.label(img)
    regions = measure.regionprops(label)

    _, left_lung_min_column, _, left_lung_max_column = regions[0].bbox
    _, right_lung_min_column, _, right_lung_max_column = regions[1].bbox
    _, heart_min_column, _, heart_max_column = regions[2].bbox

    lungs_width = max(left_lung_max_column, right_lung_max_column) - min(
        right_lung_min_column, left_lung_min_column
    )
    heart_width = heart_max_column - heart_min_column

    return {
        "id": heart.id,
        "label": heart.is_cardiomegalia(),
        "lungs_width": lungs_width,
        "heart_width": heart_width,
    }
