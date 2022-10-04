#!/usr/bin/python3
"""Validator functions"""


def is_integer(value, name="value"):
    """Check if value is an integer"""
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))


def is_positive_integer(value, name="value"):
    """Check if value is a positive integer"""
    is_integer(value, name)
    if value <= 0:
        raise ValueError("{} must be > 0".format(name))


def is_non_negative_integer(value, name="value"):
    """Check if value is a non negative integer"""
    is_integer(value, name)
    if value < 0:
        raise ValueError("{} must be >= 0".format(name))
