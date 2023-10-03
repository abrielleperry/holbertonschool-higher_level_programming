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

    @classmethod
    def save_to_file(cls, list_objs):
        """class method to save list tof instances to json file

        Args:
            list_objs (list): list of instances to be saved to file,
            if none an empty list will be saved
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """static method to convert json str representation to list

        Args:
            json_string (str): json str to convert

        Returns:
            list: list of dictionaries represented by the json str
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_instance = cls(0, 1)
        elif cls.__name__ == "Square":
            new_instance = (1)
            return new_instance
