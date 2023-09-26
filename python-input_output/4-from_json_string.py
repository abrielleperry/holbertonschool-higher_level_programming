#!/usr/bin/Python3
"""Write a function that returns an object
(Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """returns object to represented jsonstring

    Args:
        my_str (str): json string

    Returns:
        json_obj : object represented by json strong
    """
    json_obj = json.loads(my_str)
    return json_obj
