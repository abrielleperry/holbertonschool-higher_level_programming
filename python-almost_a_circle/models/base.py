#!/usr/bin/python
""" class Base that will be used as a
template for creating other subclasses
"""


class Base:
    __nb_objects = 0
"""
     keeps track of number of objects created from this class
"""

def __init__(self, id=None):
    """
        __init__:
        Initializes new instance of Base class

        Args:
        id (int): Int value set as unique id
        if not provided set to number of objects created
    """
    if id is not None:
            self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
