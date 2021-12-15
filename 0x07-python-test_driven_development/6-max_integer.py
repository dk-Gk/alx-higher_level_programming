#!/usr/bin/python3
"""Max_integer"""
def max_integer(list=[]):
    """ add Unittests"""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
