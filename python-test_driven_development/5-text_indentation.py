#!/usr/bin/python3

"""Function that prints a text with 2 new lines after
each of these characters '., ?, :'"""

def text_indentation(text):
    """Return text with 2 new lines after some characters"""
    if type(text) != str:
        raise TypeError("text must be a string")

    indent_characters = ".?:"
    new_text = ""
    for char in text:
        new_text += char
        if char in indent_characters:
            new_text += "\n\n"

    print(new_text.strip(), end="")
