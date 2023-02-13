#!/usr/bin/python3

"""Function that prints a square with the charcter #"""


def print_square(size):
    """Return square"""
    if type(size) != int:
        if type(size) == float and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
