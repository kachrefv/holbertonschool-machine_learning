#!/usr/bin/env python3
"""Calculate the shape of a matrix.

The module provides a single function `matrix_shape` which returns the
dimensions of a nested list (matrix) as a list of integers.
"""

def matrix_shape(matrix):
    shape = []
    m = matrix
    while isinstance(m, list):
        shape.append(len(m))
        if len(m) == 0:
            break
        m = m[0]
    return shape
