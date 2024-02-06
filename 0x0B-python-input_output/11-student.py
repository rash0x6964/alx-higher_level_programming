#!/usr/bin/python3
"""Define a class student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation method

        Args:
            first_name:
            last_name:
            age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation
            of a Student instance.
        """
        if attrs is not None:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance

        Args:
            json: dictionary
        """
        self.__dict__ = json
