#!/usr/bin/Python3
"""Write a function that returns an object
(Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    json_obj = json.loads(my_str)
    return json_obj
