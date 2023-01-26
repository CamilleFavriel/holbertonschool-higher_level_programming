#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for val in matrix:
        print('\t'.join(map(str, val)))
