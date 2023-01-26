#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lines in matrix:
        for i, val in enumerate(lines):
                print("{:d}".format(val), end=" " if i < len(lines) - 1 else "\n")
