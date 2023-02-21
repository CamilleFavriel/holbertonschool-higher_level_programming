#!/usr/bin/python3
""" Base Class """
__nb_objects = 0

class Base:
    """ Base Class """
    def __init__(self, id=None):
        if id is None:
            self.id = id
        for objs in range(__nb_objects):
            objs = id
