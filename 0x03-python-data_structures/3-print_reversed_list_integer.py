#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    for x in reversed(my_list):
        print("{:d}".format(x))