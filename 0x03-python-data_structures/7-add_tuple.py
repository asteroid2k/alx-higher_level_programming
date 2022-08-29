#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    res = [0, 0]
    for x in range(2):
        a = tuple_a[x:][0] if tuple_a[x:] else 0
        b = tuple_b[x:][0] if tuple_b[x:] else 0
        res[x] = a + b
    return tuple(res)
