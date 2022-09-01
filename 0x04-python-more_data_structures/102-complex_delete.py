#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value in a_dictionary.values():
        return a_dictionary
    del_keys = [k for k, v in a_dictionary.items() if v == value]
    for k in del_keys:
        del a_dictionary[k]
    return a_dictionary
