#!/usr/bin/Python3
"""a class Rectangle that inheritates from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class reping a rectangle with private width and heoghth attributes"""

    def __init__(self, width, height):
        """initalizing a rectangle with private width and heoghth attributes

        Args:
            width (int)
            height (int)
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[rectangle] {}/{}".format(self.__width, self.__height)
