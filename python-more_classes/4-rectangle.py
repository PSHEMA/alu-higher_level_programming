#!/usr/bin/python3
""" Module that defines a Rectangle class """


class Rectangle:
    """ Defines a Rectangle """

    def __init__(self, width=0, height=0):
        """ Initializes a Rectangle with an optional width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the Rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns the height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the Rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """ Returns a string representation of the Rectangle using '#' """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """ Returns a string representation of the Rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)
