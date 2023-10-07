#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        index = 0
        for n in sublist:
            if index != len(sublist) - 1:
                print('{:d}'.format(n), end=' ')
            else:
                print('{:d}'.format(n), end='')
            index += 1
        print()
