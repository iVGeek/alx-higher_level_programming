#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        mat = []
        for line in matrix:
            a = []
            for n in line:
                a.append(n**2)
            mat.append(a)
        return(mat)
