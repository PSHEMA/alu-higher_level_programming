#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = my_list[0]
    for number in my_list:
        if number > maximum:
            maximum = number
    if len(my_list) == 0:
        return None
    else:
        return maximum
