#!/usr/bin/Python3
"""a class Rectangle that inheritates from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class reping a rectangle with private width and heoghth attributes"""

    def __init__(self, size):
        """initializing a square with private size and
        validating size is postitive integer with integer_validator

        Args:
            size (int)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """_summary_

        Returns:
            str: a string of the squares format with width and height
        """
        print("[Square] {}/{}"
                .format(self._Rectangle__width, self._Rectangle__height))
