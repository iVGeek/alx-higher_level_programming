#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    taille = len(matrix[0])
    if taille != 0:
        for ligne in matrix:
            for i in range(taille - 1):
                print("{:d}".format(ligne[i]), end=" ")
            print("{:d}".format(ligne[taille - 1]))
    else:
        print("")
