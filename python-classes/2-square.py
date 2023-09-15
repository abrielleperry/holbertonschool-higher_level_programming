#!/usr/bin/Python3
"""this file will write a class Square that define a square based on 1-square.py"""

class Square:
    """empty class to define Square"""
    def __init__(self, size=0):
        for size:
        try:
            size == int
            if size != int:
                except: 
            raise TypeError("size must be an integer")
        if size < 0:
                except: raise ValueError("size must be >= 0")
