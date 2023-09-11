#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        list_len = len(row)
        if list_len == 0:
            print()
            continue
        for num in range(0, list_len - 1):
            print("{:d}".format(row[num]), end=" ")
        print("{:d}".format(row[list_len - 1]))
