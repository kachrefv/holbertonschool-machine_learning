#!/usr/bin/env python3
"""Add two arrays element-wise.

The module provides a single function `add_arrays` which returns
the element-wise sum of two arrays, or None if shapes don't match.
"""


def add_arrays(arr1, arr2):
    """Return the element-wise sum of two arrays.

    Args:
        arr1: A list of ints/floats.
        arr2: A list of ints/floats.

    Returns:
        A new list with element-wise sums, or None if arrays have different lengths.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
