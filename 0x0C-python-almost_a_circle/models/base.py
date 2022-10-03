#!/usr/bin/python3

"""Module that defines base class"""


class Base():
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        self.inc_count()
        if id is not None:
            self.id = id
        else:
            self.id = self.__nb_objects

    @classmethod
    def inc_count(cls):
        cls.__nb_objects += 1
