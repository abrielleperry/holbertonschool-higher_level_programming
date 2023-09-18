#!/usr/bin/Python3
"""file will write a class Sqaure defining a square based on 5-square.py"""


class Square:
    """initializing a Sqaure object"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be >= 0")
        elif calue < 0:
            raise ValueError("size must be an interger")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __init__(self, position=0):
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(position, tuple) or len(dimentions) != 2:
            raise TypeError("position must be tuple of 2 positive integers")
    self.__position = value

    def position(self):
        return self.__position

    def my_print(self):
        for _ in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
