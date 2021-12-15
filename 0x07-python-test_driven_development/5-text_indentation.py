#!/usr/bin/python3
"""text_identation"""
def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    check = 0
    for i in text:
        if check == 0:
            if i == ' ':
                continue
            else:
                check = 1
        if check == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                check = 0
            else:
                print(i, end="")
