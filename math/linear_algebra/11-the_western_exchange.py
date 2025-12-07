#!/usr/bin/env python3
"""Transpose a numpy array.

The module provides a single function `np_transpose` which returns
the transpose of a numpy.ndarray as a new array.
"""


def np_transpose(matrix):
    """Return the transpose of a numpy array.

    Args:
        matrix: A numpy.ndarray or array-like object.

    Returns:
        A new numpy.ndarray with axes reversed.
    """
    return matrix.T
