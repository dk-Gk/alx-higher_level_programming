#!/usr/bin/python3
"""Student class"""


class Student:
    """A class representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and
            all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
