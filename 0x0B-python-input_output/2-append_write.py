#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """appends filename with utf-8"""
    with open(filename, 'a', encoding="utf-8") as fd:
        return fd.write(text)
