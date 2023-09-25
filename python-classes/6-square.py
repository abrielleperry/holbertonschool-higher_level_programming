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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be an >= 0")
        self.__size = value
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be tuple of 2 positive integers")
    self.__position = value


    def area(self):
        return self__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__position[0]) + "#" * self.__size:
                print(" " * self.__position[0] + "#" * self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be >= 0")
        elif calue < 0:
            raise ValueError("size must be an interger")
        self.__size = value

    def position(self):
        return self.__position

    def __init__(self, position=0):
        self.__position = position

    @property
    def position(self):
        return self.__position


    def position(self):
        return self.__position
