#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    a = my_list
    a.sort
    return a[-1]
