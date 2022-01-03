#!/usr/bin/python3
"""class Base"""
import json
import csv
import turtle

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
        d = []
        try:
            with open(fname) as f:
                d = cls.from_json_string(f.read())
            for key, value in enumerator(d):
                d[key] = cls.create(**d[key])
        except:
            pass
        return d

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv"""
        if (list_objs is None or not isinstance(list_objs, list)
            or not all(isinstance(j, Base) for j in list_objs)):
            with open(cls.__name__ + ".csv", "w") as file:
                file.write("[]")
            if list_objs and any(isinstance(j, Base) for j in list_objs):
                dict_data = [i.to_dictionary() for i in list_objs]
                if cls.__name__ == "Rectangle":
                    csv_columns = ["id", "width", "height", "x", "y"]
                else:
                    csv_columns = ["id", "size", "x", "y"]
                with open(cls.__name__ + ".csv", "w") as file:
                    writer = csv.DictWriter(file, fieldnames=csv_columns)
                    writer.writeheader()
                    for data in dict_data:
                        writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file"""
        list_instance = []
        name = cls.__name__ + ".csv"
        if os.path.isfile(name):
            with open(name, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    d = {key: int(value) for key, value in row.items()}
                    list_instance.append(cls.create(**d))
            return list_instance
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws sqaures and rectangles"""
        for i in list_rectangles + list_squares:
            tt = turtle.Turtle()
            tt.shape("turtle")
            turtle.bgcolor("black")
            tt.fillcolor("white")
            tt.begin_fill()
            tt.pen(fillcolor="white", pencolor="red", pensize=2)
            for _ in range(2):
                tt.forward(i.width)
                tt.right(90)
                tt.forward(i.height)
                tt.right(90)
            tt.end_fill()
            turtle.done()
