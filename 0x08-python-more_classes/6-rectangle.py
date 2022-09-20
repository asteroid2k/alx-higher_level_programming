#!/usr/bin/python3

""" Module that defines a class Rectangle """


class Rectangle:
    """This is a class that defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """This is the initialization of the class"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This is the getter of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is the getter of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This is the getter of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is the setter of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This is the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This is the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def print(self):
        """This is the print of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            print()
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        rec_str = ""
        """This is the print of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return rec_str
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += "#"
            rec_str += "\n" if i != self.__height - 1 else ""
        return rec_str

    def __repr__(self) -> str:
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        del self
        Rectangle.number_of_instances -= 1
