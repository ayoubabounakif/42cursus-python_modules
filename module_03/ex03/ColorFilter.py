import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load(path):
    try:
        with Image.open(path) as img:
            width, height = img.size
            print(f"Image dimensions: {width} x {height}")
            return np.asarray(img)
    except FileNotFoundError as e:
        print(e)
    except OSError as e:
        print(e)

class ColorFilter:

    def __init__(self):
        pass

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        
        Args:
        -----
        array: numpy.ndarray corresponding to the image.

        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.

        Raises:
        -------
        This function should not raise any Exception.
        """
        inverted_array = np.copy(array)
        for i in range(3):
            inverted_array[:, :, i] = 255 - inverted_array[:, :, i]
        return inverted_array

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.

        Args:
        -----
        array: numpy.ndarray corresponding to the image.

        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.

        Raises:
        -------
        This function should not raise any Exception.
        """
        blue_array = np.copy(array)
        blue_array[:, :, 0] = 0
        blue_array[:, :, 1] = 0
        return blue_array

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.

        Args:
        -----
        array: numpy.ndarray corresponding to the image.

        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.

        Raises:
        -------
        This function should not raise any Exception.
        """
        green_array = np.copy(array)
        green_array[:, :, 0] = 0
        green_array[:, :, 2] = 0
        return green_array

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        red_array = np.copy(array)
        red_array[:, :, 1] = 0
        red_array[:, :, 2] = 0
        return red_array


    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.

        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.

        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.

        Raises:
        -------
        This function should not raise any Exception.
        """

        grayscale_array = np.copy(array)
        if filter == 'mean' or filter == 'm':
            # rgb2gray converts RGB values to grayscale values by forming a weighted sum of the R, G, and B components: 0.2989 * R + 0.5870 * G + 0.1140 * B 
            Ylinear = [0.2989, 0.5870, 0.1140] # Gray
            grayscale_array = np.sum(grayscale_array[...,:3] * Ylinear, axis=-1)
        elif filter == 'weight' or filter == 'w':
            grayscale_array = np.sum(grayscale_array[...,:3] * kwargs['weights'], axis=-1)
        return grayscale_array

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.

        Args:
        -----
        array: numpy.ndarray corresponding to the image.

        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.

        Raises:
        -------
        This function should not raise any Exception.
        """
        celluloid_array = np.copy(array)
        midpoints = [0, 85, 170, 255]
        limits = [(0, 64), (64, 128), (128, 192), (192, 256)]
        for i, (low, high) in enumerate(limits):
            interval = np.arange(low, high)
            interval_min = np.min(interval)
            interval_max = np.max(interval)
            celluloid_array[(celluloid_array > interval_min) & (celluloid_array <= interval_max)] = midpoints[i]
        return celluloid_array

if __name__ == "__main__":

    # array = np.array([[
    #     [255, 0, 0],
    #     [0, 255, 0],
    #     [0, 0, 255]],
    #     [
    #     [255, 255, 0],
    #     [255, 0, 255],
    #     [0, 255, 255]],
    #     [
    #     [255, 255, 255],
    #     [128, 128, 128],
    #     [0, 0, 0]]
    # ])

    # print(array)
    # print(array[:, :, 0]) # Red channel
    # print(array[:, :, 1]) # Green Channel
    # print(array[:, :, 2]) # Blue Channel

    cf = ColorFilter()
    
    # for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
    #     array = load("../resources/elon_canaGAN.png")
    #     plt.imshow(f(array))
    #     plt.show()

    # array = load("../resources/elon_canaGAN.png")
    # plt.imshow(cf.to_celluloid(array))
    # plt.show()

    array = load("../resources/elon_canaGAN.png")
    im = cf.to_grayscale(array, "m")
    plt.imshow(im, cmap='gray')
    plt.show()


    # im = cf.to_grayscale(array, "w", weights = [0.2, 0.3, 0.5])
    # plt.imshow(im, cmap="gray")
    # plt.show()
