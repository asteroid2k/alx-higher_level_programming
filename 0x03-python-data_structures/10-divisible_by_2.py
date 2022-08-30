#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    res = []
    for x in my_list:
        res.append(x % 2 == 0)
    return res


my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)
