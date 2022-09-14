#!/usr/bin/python3
'''Module to define a Square class'''


class Square:
    '''Represents a Square class'''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        for v in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" "*self.__position[0], "#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or value[0]+value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive")
        self.__position = value
