#!/usr/bin/python3
"""class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """call superclass constructer with id"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes new instance of Rectangle class

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x coordinate to rectangle
            y (int): y coordinate to rectangle
            id (int): id of rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def get_width(self):
        """ get_width of rectangle """
        return self.__width

    def set_width(self, width):
        """
        set_width of rectangle

        Args:
            width (int): new width of value
        """
        self.__width = width

    def get_height(self):
        """get_height of rectangle"""
        return self.__height

    def set_height(self, height):
        """
        set_height of rectangle

        Args:
            height (int): new height value
        """
        self.__height = height

    def get_x(self):
        """get_x coordinate of rectangle"""
        return self.__x

    def set_x(self, x):
        """
        set_x coordinate of rectangle

        Args:
            x (int): new x coordinate
        """
        self.__x = x

    def get_y(self):
        """get_y coordinate of rectangle"""
        return self.__y

    def set_y(self, y):
        """
        set_y coordinate of rectangle

        Args:
            y (int): new y coordinate of rectangle
        """
        self.__y = y
