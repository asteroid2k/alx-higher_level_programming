#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value in a_dictionary.values():
        return a_dictionary
    for key in a_dictionary:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
