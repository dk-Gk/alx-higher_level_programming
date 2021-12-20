#!/usr/bin/python3
"""class BaseGeometry"""
class BaseGeometry:
    """A class with area and integer_validator methods"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates the inputs: name and values"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
