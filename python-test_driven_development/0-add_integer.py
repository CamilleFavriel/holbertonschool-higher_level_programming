#!/usr/bin/python3

"""Function that adds 2 integers."""


def add_integer(a, b=98):
    """Returns added integers."""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or a float")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer or a float")
    a = int(a)
    b = int(b)
    return a + b
