#!/usr/bin/Python3
"""this is a file that will write  a function that prints
a square with the character #"""

def print_square(size):
    """print_square function take int and prints size of square with hash"""
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0:
        raise TypeError("size must be an integer")
    
    square = "#" * size
    for _ in range(size):
        print("{}".format(square))