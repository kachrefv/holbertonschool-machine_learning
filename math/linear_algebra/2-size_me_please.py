#!/usr/bin/env python3
"""Calculate the shape of a matrix.

This module provides a function to determine the dimensions of a nested
list (matrix) structure.
"""


def matrix_shape(matrix):
    shape = []  # matrix shape
    m = matrix  # temporary variable
    while isinstance(m, list):
        shape.append(len(m))  # append current dimension size
        if len(m) == 0:
            break  # empty list, stop here
        m = m[0]  # go one level deeper
    return shape  # return shape
