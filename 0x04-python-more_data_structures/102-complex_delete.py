#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value in a_dictionary.values():
        return a_dictionary
    copyd = a_dictionary.copy()
    for key in a_dictionary:
        if copyd[key] == value:
            del copyd[key]
    return copyd
