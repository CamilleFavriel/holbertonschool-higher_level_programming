#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary.items():
# When looping through dictionaries, the key and corresponding 
# value can be retrieved at the same time using the items() method.
        new_dict[key] *= 2
    return new_dict
