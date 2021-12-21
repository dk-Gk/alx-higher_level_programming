#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """reads filename with utf-8"""
    with open(filename, encoding='utf-8') as rd:
        print(rd.read(), end="")
