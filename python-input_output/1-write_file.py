#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)
    and returns the number of characters written:summary_"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
