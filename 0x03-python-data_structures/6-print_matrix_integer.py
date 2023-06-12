#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in the range(len(matrix)):
        for j in the range(len(matrix[i])):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()
