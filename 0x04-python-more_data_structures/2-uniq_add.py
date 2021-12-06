#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    s = list(set(my_list))
    for i in range(len(s)):
        res = res + s[i]
    return res
