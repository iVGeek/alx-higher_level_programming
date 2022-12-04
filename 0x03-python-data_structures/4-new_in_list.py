#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copie_my_list = []
    for loop in my_list:
        copie_my_list.append(loop)
    if idx >= 0 and idx < len(copie_my_list):
        copie_my_list[idx] = element
    return (copie_my_list)
