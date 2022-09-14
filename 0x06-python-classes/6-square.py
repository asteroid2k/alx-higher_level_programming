#!/usr/bin/python3
'''Module to define a Square class'''


class Square:
    '''Represents a Square class'''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        for v in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" "*self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int or int(value[0])+int(value[1]) < 0:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value
