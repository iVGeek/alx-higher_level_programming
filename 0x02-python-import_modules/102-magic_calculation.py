#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculatrice(a, b):
    if a < b:
        c = add(a, b)
        for loop in range(38, 98):
