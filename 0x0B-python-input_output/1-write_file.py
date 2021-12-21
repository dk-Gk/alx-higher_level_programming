#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """reads filename with utf-8"""
    with open(filename, "w", encoding='utf-8') as fd:
        return fd.write(text)
