#!/usr/bin/python3

"""Module for Rectangle class"""


class Rectangle():
    """Rectangle class"""

    def __init__(self, width, height):
        """__init__ method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
