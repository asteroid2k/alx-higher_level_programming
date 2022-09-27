#!/usr/bin/python3

""" Module that defines a function that returns True if
 the object is an instance the specified class """


def is_kind_of_class(obj, a_class):
    """Function that defines a function that returns True if
       the object is an instance the specified class"""
    return isinstance(obj, a_class)
