#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value in a_dictionary.values():
        return a_dictionary
    a_dictionary = {k: v for k, v in a_dictionary.items() if v != value}
    return a_dictionary
