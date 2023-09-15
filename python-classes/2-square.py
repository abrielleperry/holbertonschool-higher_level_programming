#!/usr/bin/Python3
"""this file will write a class Square that define a square based on 1-square.py"""

class Square:
    """empty class to define Square"""
    def __init__(self, size=0):
            self.__size = size
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
    """returning area of Square"""
