#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lines in range(matrix):
        for val in range(lines):
            print("{:d}".format(val), end=" ")
        print()
