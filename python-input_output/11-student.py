#!/usr/bin/python3
""" class Student that defines a student by: (based on 10-student.py) """

class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            attrs_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    attrs_dict[attr] = self.__dict__[attr]
            return attrs_dict

    def reload_from_json(self, json):
        for attr, value in json.items():
            setattr(self, attr, value)
