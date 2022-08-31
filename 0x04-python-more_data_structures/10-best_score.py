#!/usr/bin/python3

def best_score(a_dictionary):
    best_key = None
    best = -1
    if a_dictionary is None or len(a_dictionary.keys()) < 1:
        return best_key
    for k, v in a_dictionary.items():
        if v > best:
            best_key, best = k, v
    return best_key
