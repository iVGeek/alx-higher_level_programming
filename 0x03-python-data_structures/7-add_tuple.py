#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a != 0 or len_b != 0:
        if len_a == 0:
            return(tuple_b)
        if len_b == 0:
            return(tuple_a)
        if len_a > 0 and len_b > 0:
            if len_a >= 2:
                if len_b >= 2:
                    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
                else:
                    return(tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
            else:
                if len_b < 2:
                    return((tuple_a[0] + tuple_b[0], 0))
                else:
                    return(tuple_a[0] + tuple_b[0], tuple_b[1] + 0)
