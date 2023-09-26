#!/usr/bin/Python3
"""Write a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """function writing object to txt file using json rep

    Args:
        my_obj: obj written to txt file
        filename: specified txt file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
