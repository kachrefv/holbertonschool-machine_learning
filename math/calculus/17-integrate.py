#!/usr/bin/env python3
"""Module to calculate the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, (int, float)):
        return None

    # Check if all elements in poly are numbers
    for x in poly:
        if not isinstance(x, (int, float)):
            return None

    integral = [C]
    for i in range(len(poly)):
        val = poly[i] / (i + 1)
        # If result is a whole number, represent it as an integer
        if val % 1 == 0:
            val = int(val)
        integral.append(val)

    # Return smallest possible list by removing trailing zeros
    # But if the result is [0, 0], it should be [0] if C=0
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
