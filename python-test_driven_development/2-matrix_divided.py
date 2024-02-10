#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Definition of the matrix.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): Number to divide the matrix elements by.

    Return:
        New matrix with elements rounded to 2 decimal places.

    Raise:
        TypeError: if matrix is not a list of lists of integers or floats.
        ZeroDivisionError: if div is equal to zero.
    """

    for row in matrix:
        for el in row:
            if not isinstance(row, list) or not isinstance(el, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
