#!/usr/bin/python3



def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""

    for row in matrix:
        for i in row:
            if i != row[-1]:
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end="")
        print()
