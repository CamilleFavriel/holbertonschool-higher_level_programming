#!/usr/bin/python3

"""Function that adds 2 integers."""


def add_integer(a, b=98):
    """Returns added integers or error messages"""
    if type(a) not in [int, float]:
        try:
            a = int(a)
        except ValueError:
            raise TypeError("a must be an integer or a float")
    if type(b) not in [int, float]:
        try:
            b = int(b)
        except ValueError:
            raise TypeError("b must be an integer or a float")
    a = int(a)
    b = int(b)
    return a + b
