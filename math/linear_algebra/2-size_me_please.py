#!/usr/bin/env python3

def matrix_shape(matrix):
    shape = [] #matrix shape
    m = matrix
    while isinstance(m, list):
        shape.append(len(m))
        if len(m) == 0:
            break
        m = m[0]
    return shape #return shape
