#!/usr/bin/Python3
"""Writes a function that returns the JSON representation of an object (string)"""
import json

def to_json_string(my_obj):
    json_str = json.dumps(my_obj)
    return json_str
