#!/usr/bin/env python3
"""Add two matrices of any dimension.

The module provides a single function `add_matrices` which returns
the element-wise sum of two matrices of any depth, or None if shapes
don't match.
"""


def add_matrices(mat1, mat2):
    """Return the element-wise sum of two matrices.

    Args:
        mat1: A matrix (list or nested list) of ints/floats.
        mat2: A matrix (list or nested list) of ints/floats.

    Returns:
        A new matrix with element-wise sums, or None if shapes differ.
    """
    if len(mat1) != len(mat2):
        return None

    if isinstance(mat1[0], list):
        result = []
        for i in range(len(mat1)):
            sub_result = add_matrices(mat1[i], mat2[i])
            if sub_result is None:
                return None
            result.append(sub_result)
        return result
    else:
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
