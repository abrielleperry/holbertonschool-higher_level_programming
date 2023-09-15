#!/usr/bin/Python3
""""this file writes a Square that defines a square by 2-square.py"""

class Square:
    """empty class to define Square"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
            
        def area(self):
            return self.__size ** 2
"""returns area of current square"""
