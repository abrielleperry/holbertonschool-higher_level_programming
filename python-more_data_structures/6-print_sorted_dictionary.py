#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = dict(sorted(a_dictionary.key()))
    for key in sorted_keys:
        print("{}: {})".format(key, sorted_keys[key]))
