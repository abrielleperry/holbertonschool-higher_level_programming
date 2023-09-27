#!/usr/bin/Python3
"""Write a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file



    Returns:
        cont_json: obj frm json
    """
    with open(filename, "r", encoding="utf-8") as file:
        cont_json = json.load(file)
    return (cont_json)
