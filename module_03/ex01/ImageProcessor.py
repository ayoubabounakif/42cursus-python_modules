import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageProcessor:

    def __init__(self):
        pass

    def load(self, path):
        try:
            with Image.open(path) as img:
                width, height = img.size
                print(f"Image dimensions: {width} x {height}")
                return np.asarray(img)
        except FileNotFoundError as e:
            print(e)
        except OSError as e:
            print(e)
    
    def display(self, array):
        plt.imshow(array)
        plt.show()
