#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s = list(a_dictionary.keys())
    s.sort()
    for i in s:
        print("{}: {}".format(i, a_dictionary[i]))
