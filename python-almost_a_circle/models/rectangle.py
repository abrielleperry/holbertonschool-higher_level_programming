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

    @property
    def width(self):
        """ get_width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set_width of rectangle

        Args:
            width (int): new width of value
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get_height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        set_height of rectangle

        Args:
            height (int): new height value

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get_x coordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        set_x coordinate of rectangle

        Args:
            x (int): new x coordinate
        
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance (value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get_y coordinate of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        set_y coordinate of rectangle

        Args:
            y (int): new y coordinate of rectangle

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance (value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
