#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, col in enumerate(row):
            end_c = " " if idx != len(row) - 1 else ""
            print("{:d}".format(col), end=end_c)
        print()
