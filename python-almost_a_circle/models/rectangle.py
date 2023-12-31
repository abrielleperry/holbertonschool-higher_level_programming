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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates area of rectangle

        Returns:
            float: area of rectangle
        """
        return self.height * self.width

    def display(self):
        """display the rectangle using # with x and y coordinates
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """__str__ representation of rectangle

        Returns:
            _str_: string representing rectangle in format
        """
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """update attributes that are assigned to key/value arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """to_dictionary : returns dictionary representaion of rectangle

        Returns:
            dict: dictionary containing attrivutes of rectangle
        """
        return {
            "y": self.y,
            "x": self.x,
            "id": self.id,
            "width": self.width,
            "height": self.height
        }
