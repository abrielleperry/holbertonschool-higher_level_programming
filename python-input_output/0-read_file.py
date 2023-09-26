#!/usr/bin/Python3

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(file.read(), end="")
        file.close()
