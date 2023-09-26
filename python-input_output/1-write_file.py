#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)
    and returns the number of characters written:summary_"""


def write_file(filename="", text=""):
    """writes text to file w specified file name

    Args:
        filename (str): file to write to
        text (str): text being written to file

    Returns:
        numchars (int): number of characters
    """
    with open(filename, "w", encoding="utf-8") as file:
        numchars = file.write(text)
    return numchars
