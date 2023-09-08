#!/usr/bin/python3
def uppercase(str):
    new = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            new = new + (chr(ord(char) - 32))
        else:
            new += char
        print("{}".format(new))
