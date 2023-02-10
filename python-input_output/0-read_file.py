#!/usr/bin/python3
"""Method that reads a text file"""


def read_file(filename=""):
    """ Reads a text file"""
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read(), end='')
