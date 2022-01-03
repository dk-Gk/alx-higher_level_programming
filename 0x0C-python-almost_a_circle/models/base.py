#!/usr/bin/python3
"""class Base"""
import json


class Base:
    """Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """serilization of python"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        fname = cls.__name__ + ".json"
        d = []
        for l in list_objs:
            d.append(l.to_dictionary())
        with open(fname, 'w') as f:
            f.write(cls.to_json_string(d))

    def from_json_string(json_string):
        """decoding"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        fname = cls.__name__ + ".json"
        with open(fname) as f:
            return json.load(f)
