#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        a = ""
        for i in a_dictionary:
            big = a_dictionary[i]
            a = i
        for i in a_dictionary:
            if a_dictionary[i] > big:
                big = a_dictionary[i]
                a = i
        return a
