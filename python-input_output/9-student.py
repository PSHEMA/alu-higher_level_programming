#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """A class Student"""
    def __init__(self, first_name, last_name, age):
        """Initializes instance"""
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """retrieves a dictionary representation"""
        return self.__dict__
