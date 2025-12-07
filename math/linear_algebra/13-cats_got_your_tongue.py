#!/usr/bin/env python3
"""Concatenate numpy arrays along an axis.

The module provides a single function `np_cat` which returns
the concatenation of two arrays along a specified axis.
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Return the concatenation of two arrays along an axis.

    Args:
        mat1: A numpy.ndarray or array-like object.
        mat2: A numpy.ndarray or array-like object.
        axis: The axis along which to concatenate (default 0).

    Returns:
        A new numpy.ndarray with concatenated arrays.
    """
    return np.concatenate((mat1, mat2), axis=axis)
