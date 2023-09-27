#!/usr/bin/Python3
"""Write a function that creates an Object from a “JSON file”"""
import json

def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        cont_json = file.read()
    data = filename.loads(cont_json)

class objfrmjson:
    def __init__(filename, data):

        ObjJson = objfrmjson(data)
