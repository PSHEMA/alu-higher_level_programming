#!/usr/bin/python3
"""Inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Initializes instance"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the instance"""
        return (self.__size)**2
