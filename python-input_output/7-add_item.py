#!/usr/bin/python3
"""Write a script that adds all arguments
to a Python list, and then save them to a file"""
import json
from sys import argv
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

try:
    load("add_item.json")

except Exception as e:
    new_list = []

for obj in argv[1:]:
    new_list.append(obj)

    save(new_list, "add_item.json")
