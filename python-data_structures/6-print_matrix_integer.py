#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lines in matrix:
        for i, val in lines:
            if i < len(lines) - 1:
                print("{:d}".format(val), end=" ")
        print()
