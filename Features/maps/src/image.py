import skimage.io as io
import numpy as np


# Set vmin and vmax for discrete values or we can map images form 0 to 1 and show by cmap="gray"
def show(img, only_hearths: bool = False):
    show = np.zeros_like(img)
    if only_hearths:
        show[img == 1] = 0
        show[img == 2] = 2
    else:
        show = img

    io.imshow_collection([show], cmap="gray", vmin=0, vmax=2)
    io.show()


def show_collection(collection, only_hearths: bool = False):
    show = []
    if only_hearths:
        for img in collection:
            s = np.zeros_like(img)
            s[img == 1] = 0
            s[img == 2] = 2
            show.append(s)
    else:
        show = collection

    io.imshow_collection(show, cmap="gray", vmin=0, vmax=2)
    io.show()
