#!/usr/bin/python
""" """


class Base(__nb_objects = 0):
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects 
            Base.__nb_objects += 1
