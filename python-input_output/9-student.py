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

    def to_json(self):
            """returns dictionary representation of a Student instance"""
            return self.__dict__
