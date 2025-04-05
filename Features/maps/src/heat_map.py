import numpy as np
from collections import deque
import skimage.io as io


def create_map(img, center, color=2):
    # Create a copy of the image to mark distances
    marked_img = np.zeros_like(img, np.uint16).squeeze()
    rows, cols = img.shape[:2]
    if center == None:
        return marked_img
    
    for y in range(rows):
        for x in range(cols):
            if (img[y, x] == color).all():  # Check if the pixel matches the color
                # Calculate Euclidean distance from the center
                dist = int(np.sqrt((x - center[1])**2 + (y - center[0])**2))
                marked_img[y, x] = dist
        
    return marked_img


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
                distances = np.sqrt((cords[:, 1] - x)**2 + (cords[:, 0] - y)**2)
                marked_img[y, x] = int(np.min(distances))

    return marked_img

# consider it as a DEBUG function
def show_heat_map(map):
    io.imshow(map, cmap="hot", vmax=map.max(), vmin=0)
    io.show()

def show_collection_heat_map(maps):
    io.imshow_collection(maps, cmap="hot") 
    io.show()
