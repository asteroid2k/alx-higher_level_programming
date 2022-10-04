#!/usr/bin/python3

"""Module that defines base model"""


class Base():
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        if id is not None:
            self.id = id
        else:
            self.inc_count()
            self.id = self.__nb_objects

    @classmethod
    def inc_count(cls):
        cls.__nb_objects += 1
