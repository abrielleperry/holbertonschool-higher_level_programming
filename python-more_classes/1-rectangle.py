#!/usr/bin/Python3
"""file that creates class Rectangle"""


class Rectangle:
    """empty class Rectangle"""
    def __init__(self, width=0, height=0):
        """initilizing rectangle with width and height"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """getting height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """getting width of recantangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting side value of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
