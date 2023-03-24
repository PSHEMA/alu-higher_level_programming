#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """A class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            temp = {}
            for elem in attrs:
                if type(elem) != str:
                    return self.__dict__
                if elem in self.__dict__.keys():
                    temp[elem] = self.__dict__[elem]
            return temp

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
