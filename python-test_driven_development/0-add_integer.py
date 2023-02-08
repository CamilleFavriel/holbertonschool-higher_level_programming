#!/usr/bin/python3
import doctest
def add_integer(a, b=98):
    """
    Adds two integers together
    a and b must be integers or floats, otherwise raise a TypeError exception with the message
    'a must be an integer' or 'b must be an integer'
    a and b must be casted to integers if they are float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

if __name__ == "__main__":
    doctest.testmod()
