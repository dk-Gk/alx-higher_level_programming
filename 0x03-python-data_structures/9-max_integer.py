#!/usr/bin/python3
def max_integer(my_list=[]):
    maxx = my_list[0]
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        if my_list[i] > maxx:
            maxx = my_list[i]
    return (maxx)
