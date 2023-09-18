#!/usr/bin/Python3
""""this file writes a Square that defines a square by 2-square.py"""


class Square:

    def __init__(self, size=0):
<<<<<<< HEAD
=======
        """empty class to define Square"""
        self.__size = size
>>>>>>> 8eb788fe412f435ecf90cce698cf65a719bbe97a
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must >= 0")
<<<<<<< HEAD
        self.__size = size            

    def area(self):
        return self.__size ** 2
    """returns area of current square"""
=======




    def area(self):
        """returns area of current square"""
        return self.__size**2
>>>>>>> 8eb788fe412f435ecf90cce698cf65a719bbe97a
