#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    elements = 0
    for i in range(x):
        try:
            print(f"{my_list[i]:d}", end="")
            elements += 1
        except (IndexError, TypeError):
            pass
    print()
    return elements
