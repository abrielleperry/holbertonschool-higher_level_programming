#!/usr/bin/python3
"""a function that appends a string at the end of
a text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """writes text to fie and returns character numbers

    Args:
        filename (str): file to write to
        text (str): text written to file

    Returns:
        charadded (int): number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        charsadded = file.write(text)
    return charsadded
