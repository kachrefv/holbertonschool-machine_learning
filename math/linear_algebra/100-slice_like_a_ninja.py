#!/usr/bin/env python3
"""Slice a numpy array along specific axes.

The module provides a single function `np_slice` which returns
a sliced view of a numpy array based on axis-specific slice tuples.
"""


def np_slice(matrix, axes={}):
    """Return a slice of a numpy array along specific axes.

    Args:
        matrix: A numpy.ndarray.
        axes: A dictionary where keys are axis indices and values are
              tuples representing slice objects for that axis.

    Returns:
        A new numpy.ndarray containing the sliced data.
    """
    slices = [slice(None)] * matrix.ndim
    for axis, slice_tuple in axes.items():
        if len(slice_tuple) == 1:
            slices[axis] = slice_tuple[0]
        elif len(slice_tuple) == 2:
            slices[axis] = slice(slice_tuple[0], slice_tuple[1])
        elif len(slice_tuple) == 3:
            slices[axis] = slice(slice_tuple[0], slice_tuple[1],
                                 slice_tuple[2])
    return matrix[tuple(slices)]
