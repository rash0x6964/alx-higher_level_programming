#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x * x, sub_list)) for sub_list in matrix]
