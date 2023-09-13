#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for index in range(x):
            if isinstance(mylist_[i], int):
                print("{:d}".format(my_list[i], end="\n"))
                count += 1
    except (IndexError, TypeError):
        pass
    return count



