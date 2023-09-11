#!/usr/bin/python3

def uniq_add(my_list=[]):
    get_list = []
    for num in my_list:
        if num not in get_list:
            get_list.append(num)
        else:
            continue
    sum = 0
    for num in get_list:
        sum += num
    return sum
