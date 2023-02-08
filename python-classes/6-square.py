#!/usr/bin/python3
"""
    Square is printing a square.
"""


class Square:
    """Defines a square object with size and position properties"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size property
        
        Raises:
            TypeError: If the size value is not an integer
            ValueError: If the size value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position property
        
        Raises:
            TypeError: If the position value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(
            isinstance(i, int) and i >= 0 for i in value
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
