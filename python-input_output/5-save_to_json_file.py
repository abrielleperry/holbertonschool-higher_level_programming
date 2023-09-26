#!/usr/bin/Python3
"""Write a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as file:
        objtotext = file.write(text)
        json_objtotext = json.loads(my_obj)
    return json_objtotext
    