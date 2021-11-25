#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s = list(a_dictionary.items())
    s.sort()
    s = dict(s)
    for i in s:
        print("{}: {}".format(i, s[i]))
