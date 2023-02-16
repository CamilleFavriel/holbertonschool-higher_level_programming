#!/usr/bin/python3

"""Function that returns the list of available attributes
and methods of an object"""


class MyList(list):
    """Copy of list"""

    def print_sorted(self):
        """Printsin ascending sort"""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
