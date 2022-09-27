#!/usr/bin/python3
"""Module to lookup all methods and attribute of an object"""


def lookup(obj):
    """function that returns the list of available attributes
     and methods of an object"""
    return dir(obj)
