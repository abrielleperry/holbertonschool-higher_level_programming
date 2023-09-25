#!/usr/bin/Python3
"""a module that defines the inherits_from function"""


def inherits_from(obj, a_class):
    """check if the object is exact instance of class or inherited
    (directly or indirectly) from the specified class


    Args:
        obj (object): object to check
        a_class (type): specified class to check against

    Returns: True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
