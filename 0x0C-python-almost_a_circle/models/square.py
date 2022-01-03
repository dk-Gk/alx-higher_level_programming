#!/usr/bin/python3
"""class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializaton method"""
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""

        return self.width

    @size.setter
    def size(self, s):
        """size setter"""
        self.width = s
        self.height = s

    def __str__(self):
        """string representation of square class"""

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns attributes"""

        if(len(args)):
            count = 0
            for arg in args:
                count += 1
                if count == 1:
                    self.id = arg
                if count == 2:
                    self.size = arg
                if count == 3:
                    self.x = arg
                if count == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """"returns the dictionary representation of a Square"""

        d = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return d
