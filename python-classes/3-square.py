#!/usr/bin/Python3
""""this file writes a Square that defines a square by 2-square.py"""


class Square:

    def __init__(self, size=0):
        """empty class to define Square"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must >= 0")




    def area(self):
        """returns area of current square"""
        return self.__size**2
