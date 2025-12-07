#!/usr/bin/env python3
"""Perform matrix multiplication on numpy arrays.

The module provides a single function `np_matmul` which returns
the product of two matrices using numpy.
"""

import numpy as np


def np_matmul(mat1, mat2):
    """Return the product of two matrices.

    Args:
        mat1: A numpy.ndarray (m x n matrix).
        mat2: A numpy.ndarray (n x p matrix).

    Returns:
        A new numpy.ndarray with the product (m x p matrix).
    """
    return np.matmul(mat1, mat2)
