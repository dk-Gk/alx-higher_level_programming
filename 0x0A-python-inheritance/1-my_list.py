#!/usr/bin/python3
"""MyList class"""

class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
