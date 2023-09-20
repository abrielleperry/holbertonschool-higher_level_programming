#!/usr/bin/Python3
"""this file writes a function that prints a text with 2 new
lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """text_identation prints a text with 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    check_newline = True

    for char in text:
        if char in [".", "?", ":"]:
            if check_newline:
                print("", end="\n\n")
                check_newline = False
            print(char, end="\n\n")
        else:
            print(char, end="")
            check_newline = False
