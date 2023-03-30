#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    :param list_of_integers: A list of unsorted integers.
    :return: A peak in the list of integers.
    """
    if len(list_of_integers) == 0:
        return None

    peak = list_of_integers[0]

    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]

    return peak
