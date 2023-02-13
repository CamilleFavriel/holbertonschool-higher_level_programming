#!/usr/bin/python3

"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Return Divided elements of a matrix"""
    if type(matrix) != list or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i/div, 2) for i in row] for row in matrix]
