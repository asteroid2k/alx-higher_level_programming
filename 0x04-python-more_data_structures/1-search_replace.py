#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for val in my_list:
        val = val if val != search else replace
        new_list.append(val)
    return new_list
