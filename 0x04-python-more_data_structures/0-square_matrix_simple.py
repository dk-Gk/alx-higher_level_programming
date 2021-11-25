#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        sq = list(map(lambda x: x*x, matrix[i]))
        new.append(sq)
    return new
