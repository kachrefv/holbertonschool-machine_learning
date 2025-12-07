#!/usr/bin/env python3
"""Calculate the shape of a numpy array.

The module provides a single function `np_shape` which returns
the shape of a numpy.ndarray as a tuple of integers.
"""


def np_shape(matrix):
    """Return the shape of a numpy array.

    Args:
        matrix: A numpy.ndarray.

    Returns:
        A tuple of integers representing the shape of the array.
    """
    return matrix.shape
