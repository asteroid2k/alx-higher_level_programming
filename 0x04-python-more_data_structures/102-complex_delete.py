#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value in a_dictionary.values():
        return a_dictionary
    copy = a_dictionary.copy()
    for key in a_dictionary:
        if copy[key] == value:
            del copy[key]
    return copy
