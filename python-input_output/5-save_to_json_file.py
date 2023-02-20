#!/usr/bin/python3
"""Method that appends a string at the end of a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Returns the JSOn representation of an object (string)"""
    with open("filename", "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
