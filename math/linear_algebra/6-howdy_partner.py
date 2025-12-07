#!/usr/bin/env python3
"""Concatenate two arrays.

The module provides a single function `cat_arrays` which returns
the concatenation of two arrays as a new list.
"""


def cat_arrays(arr1, arr2):
    """Return the concatenation of two arrays.

    Args:
        arr1: A list of ints/floats.
        arr2: A list of ints/floats.

    Returns:
        A new list with elements from arr1 followed by elements from arr2.
    """
    return arr1 + arr2
