#!/usr/bin/python3
def safe_print_integer(value):
    i = 0
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        return False
