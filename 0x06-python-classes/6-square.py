#!/usr/bin/python3

'''Module to define a Square class'''


class Square:
    '''Represents a Square class'''

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = ()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def position(self):
        return self.__position

    @size.position
    def position(self, value):
        self.__position = value

    def area(self):
        return

    def my_print(self):
        for i in range(self.__size):
            print("#" * self.__size)
