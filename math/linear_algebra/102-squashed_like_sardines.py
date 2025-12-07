#!/usr/bin/env python3
"""Concatenate two matrices along a specific axis.

The module provides a single function `cat_matrices` which returns
the concatenation of two matrices along a specified axis, or None if
concatenation is not possible.
"""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis.

    Args:
        mat1: A matrix (list or nested list) of ints/floats.
        mat2: A matrix (list or nested list) of ints/floats.
        axis: The axis along which to concatenate (default 0).

    Returns:
        A new matrix with concatenated data, or None if shapes are
        incompatible along the concatenation axis.
    """
    if isinstance(mat1[0], list):
        if len(mat1) != len(mat2):
            return None
        if axis == 0:
            return [row[:] for row in mat1] + [row[:] for row in mat2]
        else:
            result = []
            for i in range(len(mat1)):
                sub_result = cat_matrices(mat1[i], mat2[i], axis=axis - 1)
                if sub_result is None:
                    return None
                result.append(sub_result)
            return result
    else:
        if axis != 0:
            return None
        return mat1[:] + mat2[:]
