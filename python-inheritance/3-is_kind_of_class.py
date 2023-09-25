#!/usr/bin/Python3
"""a module that defines is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """check if obj is an instance of or if the object is an instance
    of a class that inherited from the specified class

        Args:
            obj (object): obejct to check
            a_class (type): specified class to check against

        Returns:
            bool: True if obj is an instance of or if the object is an instance
        of a class that inherited from the specified class, otherwise False
        """
    return isinstance(obj, a_class)
