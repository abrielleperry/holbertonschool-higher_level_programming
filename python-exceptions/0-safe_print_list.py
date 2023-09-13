#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i]):
                print("{:d}".format(my_list[i], end="\n"))
                count += i
    except (IndexError, TypeError):
        pass
    return x
