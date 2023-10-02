#!/usr/bin/python3
"""class Square that inherites from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class representing square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initializing new instance of square class

        Args:
            size (int): size of square
            x (int): x coordinate of square
            y (int): y coordinate of square
            id (int): id of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size gets size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """setting size for square

        Args:
            value (int): new size value
        """
        self.width = value
        self.height = value

    @property
    def width(self):
        """ get_width of square """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set_width of square

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
        set_height of square

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

    def update(self, *args, **kwargs):
        """update attributes that are assigned to key/value arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """to_dictionary: returns dictionary representaion of rectangle

        Returns:
            dict: dictionary containing attrivutes of rectangle
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
