#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a1, *a2 = tuple_a
    b1, *b2 = tuple_b
    a2 = a2[0] if a2 else 0
    b2 = b2[0] if b2 else 0
    return (a1 + b1, a2 + b2)
