#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        maxe = my_list[0]
        for n in my_list:
            if n > maxe:
                maxe = n
        return (maxe)
    return (None)
