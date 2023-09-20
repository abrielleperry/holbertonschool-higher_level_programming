#!/usr/bin/Python3
"""this file writes a function that prints a text with 2 new
lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """text_identation prints a text with 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    check_newline = False

    for char in text:
        if char in [".", "?", ":"]:
            check_newline = True
            print(char + "\n\n")
        else:
            if check_newline:
                print(char + "\n\n")
                check_newline = False
            else:
                print(char, end="")
