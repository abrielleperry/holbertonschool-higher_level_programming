#!/usr/bin/Python3
"""this file writes a function that prints a text with 2 new
lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """text_identation prints a text with 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n")
    text = text.replace("?", "?\n")
    text = text.replace(":", ":\n")

    print(text)
