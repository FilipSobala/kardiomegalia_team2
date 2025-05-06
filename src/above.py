import skimage.measure as measure
import numpy as np



def longest_vertical_line(img, color=2):
    labels = measure.label(img == color)
    regions = measure.regionprops(labels)

    # lines = np.zeros_like(img)
    img_with_lines = img.copy()

    if regions:
        length = 0
        longest_coords = None

        for region in regions:
            coords = region.coords
            for col in np.unique(coords[:, 1]):  # Iterate through unique columns
                col_coords = coords[coords[:, 1] == col]  # Get all points in the column
                if len(col_coords) > length:
                    length = len(col_coords)
                    longest_coords = col_coords

    else:
        print("No regions found in the image.")

    return longest_coords



def histogram(map, img):
    histogram = [0] * (map.max() + 1)

    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            if img[i][j] == 2:
                histogram[map[i][j]] += 1
    return histogram



def create_line_map(img, cords, color=2):
    # Create a copy of the image to mark distances
    marked_img = np.zeros_like(img, np.uint16).squeeze()
    rows, cols = img.shape[:2]

    # Convert cords to a NumPy array for vectorized operations
    cords = np.array(cords)

    for y in range(rows):
        for x in range(cols):
            if (img[y, x] == color).all():  # Check if the pixel matches the color
                # Calculate the minimum distance to any pixel in the line using vectorized operations
                distances = np.sqrt((cords[:, 1] - x) ** 2 + (cords[:, 0] - y) ** 2)
                marked_img[y, x] = int(np.min(distances))

    return marked_img


def above(heart, limit:float = 0.9):
    img = heart.get_img()
    line_v = longest_vertical_line(img)
    line_v_map = create_line_map(img, line_v)

    his = histogram(line_v_map, img)

    limit = round(limit * len(his))
    rtr = sum(his[limit:])

    return {
        "id": heart.id,
        "label": heart.is_cardiomegalia(),
        "limit": limit,
        "above": rtr,
        "max_dist": len(his),
    }
