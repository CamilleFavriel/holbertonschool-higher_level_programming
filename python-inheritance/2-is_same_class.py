#!/usr/bin/python3

"""Returns True if the object is exactly an
instance of the specified class; otherwise False."""


def is_same_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class;
    otherwise returns False.
    """
    return isinstance(obj, a_class)
