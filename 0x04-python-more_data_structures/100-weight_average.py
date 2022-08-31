#!/usr/bin/python3

def weight_average(my_list=[]):
    cum, sum = 0, 0
    if my_list is None:
        return 0
    for x, y in my_list:
        cum += x*y
        sum += y
    return cum/sum
