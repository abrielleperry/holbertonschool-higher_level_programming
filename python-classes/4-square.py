#!/usr/bin/Python3
"""This file will write a class Square that defines a square based on 3-sqaure.py"""

class Square:
    """empty class to define Square"""
    def __init__(self, size=0):

    @property
    def size(self)
    
    @value.setter
    def size(self, value)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        return (self.__size * self.__size)

