#!/usr/bin/python3
"""Method that write a string to a text file"""


def write_file(filename="", text=""):
    """returns the number of char written"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
