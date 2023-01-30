#!/usr/bin/python3
def simple_delete(a_dictionary, keys=""):
    if keys in a_dictionary is None:
        return a_dictionary
    a_dictionary.pop(keys)
    return a_dictionary
