#!/usr/bin/env python3
"""Add two 2D matrices element-wise.

The module provides a single function `add_matrices2D` which returns
the element-wise sum of two 2D matrices, or None if shapes don't match.
"""


def add_matrices2D(mat1, mat2):
    """Return the element-wise sum of two 2D matrices.

    Args:
        mat1: A 2D list of ints/floats.
        mat2: A 2D list of ints/floats.

    Returns:
        A new 2D list with element-wise sums, or None if shapes differ.
    """
    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
            for i in range(len(mat1))]
