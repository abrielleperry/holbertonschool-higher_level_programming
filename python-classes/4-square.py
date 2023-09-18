#!/usr/bin/Python3
"""file will write a class Square defining a square based on 3-sqaure.py"""


class Square:
    """initializing a Square object"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getting side length of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting side length of Square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returning area of square which is side length squared"""
        return self.__size ** 2
