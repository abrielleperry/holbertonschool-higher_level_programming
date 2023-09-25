#!/usr/bin/Python3
"""a module that creates a class BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    """base class for geometry"""
    def area(self):
        """
        Raises:
            Exception: raised if area method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checking if value is integer

        Args:
            name (string): string to check
            value (type): type to check against
        """
        if type(value) is not int:
            raise (TypeError("{} must be an integer".format(name)))
        if value <= 0:
            raise (ValueError("{} must be greater than 0".format(name)))
