#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""
import json
import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# If the file exists, load the existing data
if path.exists(filename):
    data = load_from_json_file(filename)
else:
    data = []

# Add the arguments to the list
for arg in sys.argv[1:]:
    data.append(arg)

# Save the list to the file
save_to_json_file(data, filename)
