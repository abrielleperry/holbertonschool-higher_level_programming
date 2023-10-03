#!/usr/bin/python3
"""class Base that will be used as a
template for creating other subclasses"""


import json


class Base:
    """ keeps track of number of objects created from this class """
    __nb_objects = 1

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list of dictionaries to_json_string

        Args:
            list_dictionaries (list of dict): list of dictionaries

        Returns:
            str: json string representation of list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
