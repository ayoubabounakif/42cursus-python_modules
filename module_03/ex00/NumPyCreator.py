import numpy as np
from numpy import random

class NumPyCreator:

    def __init__(self):
        self.array = None
    
    def from_list(self, lst, dtype=None):
        if not isinstance(lst, list): return None
        """
        Create an array from a list.

        Parameters
        ----------
        lst : list
            A list providing the data for the array.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.

        Returns
        -------
        out : ndarray
            Array interpretation of `lst`.  No copy is performed if the input
            is already an ndarray with matching dtype and order.  If `dtype` is
            set, a copy is always made, even if the dtype of `a` is the same as
            `dtype`.
        """
        self.array = np.array(lst, dtype)
        return self.array

    def from_tuple(self, tpl, dtype=None):
        if not isinstance(tpl, tuple): return None
        """
        Create an array from a tuple.

        Parameters
        ----------
        tpl : tuple
            A tuple providing the data for the array.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.

        Returns
        -------
        out : ndarray
            Array interpretation of `tpl`.  No copy is performed if the input
            is already an ndarray with matching dtype and order.  If `dtype` is
            set, a copy is always made, even if the dtype of `a` is the same as
            `dtype`.
        """
        self.array = np.array(tpl, dtype)
        return self.array

    def from_iterable(self, itr, dtype=None):
        if not isinstance(itr, (list, tuple)): return None
        """
        Create an array from an iterable object.

        Parameters
        ----------
        itr : iterable object
            An iterable object providing data for the array.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.

        Returns
        -------
        out : ndarray
            Array interpretation of `itr`.  No copy is performed if the input
            is already an ndarray with matching dtype and order.  If `dtype` is
            set, a copy is always made, even if the dtype of `a` is the same as
            `dtype`.
        """
        self.array = np.array(itr, dtype)
        return self.array
    
    def from_shape(self, shape, value=0, dtype=None):
        """
        Return a new array of given shape and type, filled with value.

        Parameters
        ----------
        shape : int or sequence of ints
            Shape of the new array, e.g., ``(2, 3)`` or ``2``.
        value : scalar, optional
            All elements are initialized to this value.  The default value is 0.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.

        Returns
        -------
        out : ndarray
            Array of uninitialized (arbitrary) data of the given shape,
            dtype, and order.
        """
        self.array = np.full(shape, value, dtype)
        return self.array

    def random(self, shape, dtype=None):
        """
        Return a new array of random floats in the half-open interval [0.0, 1.0)
        given shape and type, filled with value.

        Parameters
        ----------
        shape : int or sequence of ints
            Shape of the array, e.g., ``(2, 3)`` or ``2``.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.

        Returns
        -------
        out : ndarray
            Array of random floats of the given shape, dtype.
        """
        self.array = np.random.random(shape).astype(dtype)
        return self.array

    def identity(self, n, dtype=None):
        """
        Return the identity array.

        The identity array is a square array with ones on the main diagonal.

        Parameters
        ----------
        n : int
            Number of rows (and columns) in `n` x `n` output.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.

        Returns
        -------
        out : ndarray
            `n` x `n` array with its main diagonal set to one, and all other
            elements 0.
        """
        self.array = np.identity(n, dtype)
        return self.array

# if __name__ == "__main__":
#     npc = NumPyCreator()
#     print(npc.from_list([[1 ,2, 3], [6, 3, 4]])) # array([[1, 2, 3], [6, 3, 4]])
#     print(npc.from_list([[1, 2, 3], [6, 4]])) # None
#     print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]])) # array([['1','2','3'], ['a','b','c'], ['6','4','7'], dtype='<U21'])
#     print(npc.from_list(((1, 2), (3, 4)))) # None

#     # print(npc.from_tuple(("a", "b", "c")))
#     # print(npc.from_iterable(range(5)))
#     # print(npc.from_shape((3, 5)))
#     # print(npc.random((3, 5)))
#     # print(npc.identity(4))

#     print(npc.from_list("toto"))
#     print(npc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))