#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lines in matrix:
        for val in lines:
            print("{:d}".format(val), end="")
        print()
