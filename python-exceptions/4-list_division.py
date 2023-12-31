#!/usr/bin/Python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    
    try:
        for i in range(0, list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                new_list.append(result)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except TypeError:
                print("wrong type")
                new_list.append(0)
            except IndexError:
                print("out of range")
                new_list.append(0)
    finally:
        if len(new_list) < list_length:
                new_list.append(0)
        return new_list
