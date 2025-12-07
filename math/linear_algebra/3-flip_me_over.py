#!/usr/bin/env python3
"""Transpose a 2D matrix.

The module provides a single function `matrix_transpose` which returns
the transpose of a 2D matrix as a new matrix.
"""


def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix.
    
    Args:
        matrix: A 2D list representing a matrix.
    
    Returns:
        A new 2D list with rows and columns swapped.
    """
    return [list(row) for row in zip(*matrix)]
