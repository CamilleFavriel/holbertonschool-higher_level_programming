#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”:"""
    with open(filename, 'r') as f:
        json_str = f.read()
        obj = json.loads(json_str)
    return obj
