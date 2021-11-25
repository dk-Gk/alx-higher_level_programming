#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = []
    l = list(a_dictionary.items())
    for i in range(len(l)):
        new.append(l[i])
    new = dict(new)
    
