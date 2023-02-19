#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square."""

    def __init__(self, size):
        self.__size = size
        # Call the __init__ method of the Rectangle class
        # with width and height set to size, since a square has equal 
        # width and height.
        super().__init__(self.__size, self.__size)

    def area(self):
        """Return the area of the rectangle."""
        return self.__size ** 2
