#!/usr/bin/python3

def print_last_digit(number):
    numstr = abs(number) % 10
    print("{}".format(numstr), end="")
    return numstr
