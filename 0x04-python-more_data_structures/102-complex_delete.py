#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ls = list(a_dictionary.keys())
    for key in ls:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
