#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for x in reversed(my_list):
        print("{}".format(x))


print_reversed_list_integer([1, 2, 3, 4, 5])
