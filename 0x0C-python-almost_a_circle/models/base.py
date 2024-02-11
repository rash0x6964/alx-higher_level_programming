#!/usr/bin/python3
"""Define class Base"""
import json


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Create JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
            of list_objs to a file

        Args:
            list_objs: is a list of dictionaries

        Return:
            JSON string or "[]"
        """
        res = []
        if list_objs is not None:
            for obj in list_objs:
                res.append(obj.to_dictionary())

        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as f:
            f.write(Base.to_json_string(res))

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON string to an object

        Args:
            my_str: is a string representing a list
                    of dictionaries

        Return:
            return an empty list
            or list represented by json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
