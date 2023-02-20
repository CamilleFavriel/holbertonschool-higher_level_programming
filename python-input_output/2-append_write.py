#!/usr/bin/python3
"""Method that appends a string at the end of a text file"""


def write_file(filename="", text=""):
    """returns the number of char added"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
