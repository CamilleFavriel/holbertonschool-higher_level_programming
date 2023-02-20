#!/usr/bin/python3
"""function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean) for
JSON serialization of an object:"""

class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
