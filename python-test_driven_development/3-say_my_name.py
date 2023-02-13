#!/usr/bin/python3

"""Function that prints 'My name is <first name>
<last name>'"""


def say_my_name(first_name, last_name=""):
    """Check if type = string, otherwise raise TypeError."""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
