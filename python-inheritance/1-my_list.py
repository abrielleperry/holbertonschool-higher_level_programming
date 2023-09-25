#!/usr/bin/python3
"""a module that defines the print_sorted function"""


class Mylist(list):
    """Mylist inherited from list
    adds method to print list in ascending order

    Args:
        list (list): list to be inheritated from by MyList
    """
    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
