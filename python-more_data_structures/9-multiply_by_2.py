#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    values = 1

    for key, values in a_dictionary:
        new_dict[key] = values * 2
    
    return new_dict
