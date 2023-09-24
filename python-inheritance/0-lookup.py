#!/usr/bin/Python3
"""this file creates a function that returns
a list of available attributes and methods of an object"""


def lookup(obj):
    """getting list of available attributes and methods of an object

    Args:
        obj (object): the object to retrieve attribures and methods

    Returns:
        list: list of available attributes and methods of an object
    """
    return dir(obj)