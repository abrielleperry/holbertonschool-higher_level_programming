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

    def to_json(self, attrs):
        """returns dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__

        attr_diction = {}
        for attr in attrs:
            if hasattr(self, attr):
                attr_diction[attr] = getattr(self, attr)
        return attr_diction
