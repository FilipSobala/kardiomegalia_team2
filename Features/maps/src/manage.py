from src.heart import Heart
import numpy as np
import nibabel as nib
import os


def create_id(name):
    id = ""
    numbers = "0123456789"
    for n in name:
        if numbers.find(n) != -1:
            id += n
    return id

# Usage of class for future development like adding labels and features for each image
# Data loader prepers data for further processing mostly by getting data from Nifity files to normal files and removing additional dimension
class DataLoader():
    def __init__(self, img_res=(512, 512)):
        self.img_res = img_res
        self.data = []

    def load_data(self, input_path):
        names = os.listdir(input_path)
        for name in names:
            path = os.path.join(input_path, name)

            nifti_img = nib.load(path)
            img = np.array(nifti_img.dataobj)  
            img = img.squeeze()

            heart = Heart(img, id = create_id(name), state=False, img_res=self.img_res)
            #sprint(f"Loaded {heart.id} with name {name}")
                  
            self.data.append(heart)



    def get_data(self):
        return self.data
    
    def get_images(self):
        images = [heart.img for heart in self.data]
        return images


