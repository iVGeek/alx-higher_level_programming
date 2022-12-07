#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list:
        black_list = []
        som = 0
        for n in my_list:
            if n not in black_list:
                som += n
                black_list.append(n)
        return(som)
