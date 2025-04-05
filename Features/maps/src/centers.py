import skimage.measure as measure
import numpy as np
import cv2


def longest_horizontal_line(img, color=2):
    labels = measure.label(img == color)
    regions = measure.regionprops(labels)

    labels = measure.label(img == color)
    regions = measure.regionprops(labels)

    # lines = np.zeros_like(img)
    img_with_lines = img.copy()

    if regions:
        length = 0
        longest_coords = None

        for region in regions:
            coords = region.coords
            for row in np.unique(coords[:, 0]):  # Iterate through unique rows
                row_coords = coords[coords[:, 0] == row]  # Get all points in the row
                if len(row_coords) > length:
                    length = len(row_coords)
                    longest_coords = row_coords

    else:
        print("No regions found in the image.")

    return longest_coords


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

# Maybe add debug with drawing the lines
def cross_center(img, color=2):   
    longest_line_horizontal_coords = longest_horizontal_line(img, color)
    longest_vertical_coords = longest_vertical_line(img, color)

    for point_h in longest_line_horizontal_coords:
        for point_v in longest_vertical_coords:
            if point_h[0] == point_v[0] and point_h[1] == point_v[1]:
                return tuple(point_h[0:2])

    return None

def symetric_center(img, color=2):
    longest_line_horizontal_coords = longest_horizontal_line(img, color)
    longest_vertical_coords = longest_vertical_line(img, color)

    horizontal_midpoint = np.mean(longest_line_horizontal_coords, axis=0).astype(int)
    vertical_midpoint = np.mean(longest_vertical_coords, axis=0).astype(int)
    symmetric_center = (vertical_midpoint[0], horizontal_midpoint[1])

    return symmetric_center

