#!/usr/bin/env python3
"""Concatenate two 2D matrices along an axis.

The module provides a single function `cat_matrices2D` which returns
the concatenation of two 2D matrices along axis 0 or 1, or None if
concatenation is not possible.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Return the concatenation of two 2D matrices along an axis.

    Args:
        mat1: A 2D list of ints/floats.
        mat2: A 2D list of ints/floats.
        axis: 0 to concatenate along rows, 1 to concatenate along columns.

    Returns:
        A new 2D list with concatenated matrices, or None if incompatible.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [list(row) for row in mat1] + [list(row) for row in mat2]
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [list(mat1[i]) + list(mat2[i]) for i in range(len(mat1))]
    return None
