#!/usr/bin/Python3
"""this file will write a function that prints My name is with
the first name and last name"""


def say_my_name(first_name, last_name=""):
    """say_my_name will return string of first and last name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {}".format(first_name + " " + last_name))
