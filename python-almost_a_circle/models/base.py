#!/usr/bin/python3
""" Base Class """


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        for objs in range(Base.__nb_objects):
            objs = id
