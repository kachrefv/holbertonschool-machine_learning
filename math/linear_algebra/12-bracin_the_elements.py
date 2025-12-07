#!/usr/bin/env python3
"""Perform element-wise operations on numpy arrays.

The module provides a single function `np_elementwise` which returns
a tuple of element-wise sum, difference, product, and quotient.
"""

import numpy as np


def np_elementwise(mat1, mat2):
    """Return element-wise operations on two arrays.

    Args:
        mat1: A numpy.ndarray or array-like object.
        mat2: A numpy.ndarray or array-like object.

    Returns:
        A tuple containing (sum, difference, product, quotient) arrays.
    """
    mat1 = np.asarray(mat1)
    mat2 = np.asarray(mat2)
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
