#!/usr/bin/Python3
"""Write a class Student that defines a student """


class Student:
    """initialing public instance attributes

    Args:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            value = {
                attr: getsttr(self, attr)
                for attr in attrs
            }
            return value

        attrdict = {}
        for attr in attrs:
            if hasattr(self, attr):
                attrdict[attr] = getattr(self, attr)
        return attrdict
