#!/usr/bin/env python3
"""Perform matrix multiplication.

The module provides a single function `mat_mul` which returns
the product of two matrices, or None if multiplication is not possible.
"""


def mat_mul(mat1, mat2):
    """Return the product of two matrices.

    Args:
        mat1: A 2D list of ints/floats (m x n matrix).
        mat2: A 2D list of ints/floats (n x p matrix).

    Returns:
        A new 2D list with the product (m x p matrix), or None if
        the number of columns in mat1 does not equal the number of
        rows in mat2.
    """
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
             for j in range(len(mat2[0]))] for i in range(len(mat1))]
