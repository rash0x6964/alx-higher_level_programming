#!/usr/bin/python3
"""
    Defines a matrix division function.
"""


def matrix_divided(matrix, div):
    """Returns a new matrix, Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    if not isinstance(matrix, list) or matrix == [] or not all(
        isinstance(row, list) and all(
            isinstance(element, (int, float)) for element in row
        ) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of\
                         integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda item: round(item / div, 2), row))
            for row in matrix])
