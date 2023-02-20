#!/usr/bin/python3
"""Method that appends a string at the end of a text file"""
import json


def to_json_string(my_obj):
    """Returns the JSOn representation of an object (string)"""
    return json.dumps(my_obj)
