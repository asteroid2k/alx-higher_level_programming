#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    res = []
    for i in range(len(matrix)):
        res.append(list(range(0, len(matrix[i]))))
        for j in range(len(matrix[i])):
            res[i][j] = matrix[i][j] ** 2
    return res
