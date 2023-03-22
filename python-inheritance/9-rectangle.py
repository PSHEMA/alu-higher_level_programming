#!/usr/bin/python3
"""Inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geomrtry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherited from BaseGeometry"""
    def __init__(self. width, height):
        """ Initializes instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the are of the instance"""
        return self.__width*self.__height

    def __str__(self):
        """return a printable string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
