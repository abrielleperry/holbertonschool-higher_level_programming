#!/usr/bin/python3

def uppercase(str):
    upstr = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upstr = upstr + (chr(ord(char) - 32))
        else:
            upstr += char
    print("{}".format(upstr))
