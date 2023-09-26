#!/usr/bin/Python3
"""Writes a function that returns the JSON representation of an object (string)"""
import json

def to_json_string(my_obj):
    """function representing an object

    Args:
        my_obj (obj): reprentation of object

    Returns:
        json_str (str): json string
    """
    json_str = json.dumps(my_obj)
    return json_str
