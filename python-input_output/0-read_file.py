#!/usr/bin/Python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """reads text file

    Args:
        filename (str, optional): file to write to
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
