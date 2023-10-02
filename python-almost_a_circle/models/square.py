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
