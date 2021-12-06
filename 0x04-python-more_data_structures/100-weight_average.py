#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    s = 0
    if len(my_list) == 0:
        return (0)
    for i in my_list:
        res += (i[0] * i[1])
        s += i[1]
    return (res / s)
