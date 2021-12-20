#!/usr/bin/python3

"""class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inheritsfrom the BaseGeometry"""
    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
        
    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """Return the print() and str()representation of a Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
