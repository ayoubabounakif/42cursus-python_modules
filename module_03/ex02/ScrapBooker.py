import numpy as np

class ScrapBooker:

    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.

        Args
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.

        Return
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).

        Raise
        ------
        This function should not raise any Exception.
        """
        row_start, row_end = position[0], position[0] + dimensions[0]
        col_start, col_end = position[1], position[1] + dimensions[1]
        if row_end > array.shape[0] or col_end > array.shape[1]:
            return None
        return array[row_start:row_end, col_start:col_end]

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)

        Args
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.

        Return
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).

        Raise
        ------
        This function should not raise any Exception.
        """
        if axis != 0 and axis != 1:
            return None
        if n < 1 or n > array.shape[axis]:
            return None
        return np.delete(array, np.s_[n-1::n], axis)

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.

        Args
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.

        Return
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).

        Raises
        -------
        This function should not raise any Exception.
        """
        if axis != 0 and axis != 1:
            return None
        if n < 1:
            return None
        return np.concatenate([array] * n, axis)

    def mosaic(self, array, dimensions):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.

        Args
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.

        Return
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).

        Raises
        -------
        This function should not raise any Exception.
        """        
        pass

if __name__ == '__main__':
    x = ScrapBooker()
    matrix = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]])
    
    # print('--------- 5x5 ---------')
    # print(matrix)

    # print('------ 3x3 starting (1, 1) ------')
    # submatrix = x.crop(matrix, (3, 3), (1, 1))
    # print(submatrix)

    # print('------ 2x2 starting (2, 2) ------')
    # submatrix = x.crop(matrix, (2, 2), (2, 2))
    # print(submatrix)

    # print('------ 10x10 starting (0, 0) ------')
    # submatrix = x.crop(matrix, (10, 10), (0, 0)) # Not compatible with the size of the original matrix
    # print(submatrix)

    # arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    # print(x.thin(arr2, 3, 0))

    # arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
    # print(x.thin(arr3 3, 1))


    arr7 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(x.juxtapose(arr7, 3, 1))