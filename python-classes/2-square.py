#!/usr/bin/python3
"""
    Square is printing a square.
"""


class Square:
    """
    A class representing a square.
    """
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
