#!/usr/bin/Python3
def list_division(my_list_1, my_list_2, list_length):
    
    new_list = []
    for i in range(0, len(my_list_1)):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
    if len(new_list) < list_length:
            new_list.append(0)
    return new_list
        


