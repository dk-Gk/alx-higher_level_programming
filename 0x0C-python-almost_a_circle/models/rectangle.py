#!/usr/bin/python3
"""class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializaton method"""

        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, w):
        """width setter"""

        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        elif w < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = w

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, h):
        """height setter"""

        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        elif h < 1:
            raise ValueError("height must be > 0")
        else:
            self.__height = h

    @property
    def x(self):
        """x getter"""

        return self.__x

    @x.setter
    def x(self, v):
        """x setter"""

        if not isinstance(v, int):
            raise TypeError("x must be an integer")
        elif v < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = v

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, v):
        """y setter"""

        if not isinstance(v, int):
            raise TypeError("y must be an integer")
        elif v < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = v

    def area(self):
        """"returns the area value of the Rectangle"""

        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" "*self.x, end="")
            print("#"*self.width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height> form"""

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        if(len(args)):
            count = 0
            for arg in args:
                count += 1
                if count == 1:
                    self.id = arg
                if count == 2:
                    self.width = arg
                if count == 3:
                    self.height = arg
                if count == 4:
                    self.x = arg
                if count == 5:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        d = {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}
        return d
