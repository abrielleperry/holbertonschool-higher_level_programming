#!/usr/bin/Python3
"""file will write a class Square defining a squared based on 4-square.py"""


class Square:
    """initialzing a Square object"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be >= 0")
        elif value < 0:
            raise ValueError("size must be an integer")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        
