#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    max = my_list[0]
    for x in my_list:
        max = x if max < x else max
    return max
