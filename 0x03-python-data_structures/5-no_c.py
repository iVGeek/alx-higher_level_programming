#!/usr/bin/python3

def no_c(my_string):
    return("".join([c if c not in "cC" else '' for c in my_string]))
