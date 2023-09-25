#!/usr/bin/Python3
"""a module that defines the is_same_class function"""


def is_same_class(obj, a_class):
    """check if the object is exact instance of class

    Args:
        obj (object): object to check
        a_class (type): specified class to check against

    Returns:
        bool: True if obj is exact instance of a_class, otherwise False
    """
    return type(obj) is a_class
