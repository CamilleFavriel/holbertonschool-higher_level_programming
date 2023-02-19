#!/usr/bin/python3
"""
This module defines a Rectangle class
that inherits from the BaseGeometry class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        self.__width = None
        self.__height = None
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
