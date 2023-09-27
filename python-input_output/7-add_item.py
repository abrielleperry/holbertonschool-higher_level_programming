#!/usr/bin/python3
"""Write a script that adds all arguments
to a Python list, and then save them to a file"""
import json
from sys import argv
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

try:
    content = load("add_item.json")

except FileNotFoundError:
    content = []

for arg in argv[1:]:
    content.append(arg)

    save(content, "add_item.json")
