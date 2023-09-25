#!/usr/bin/Python3
"""a module that creates a class BaseGeometry based on 5-base_geometry.py"""


class BaseGeometry:
    """ base class for geometry
    """
    def area(self):
        """
        Raises:
            Exception: raised if area method is not implemented
        """
        raise Exception("area() is not implemented")
