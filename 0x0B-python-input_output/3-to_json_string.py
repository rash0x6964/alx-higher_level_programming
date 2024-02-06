#!/usr/bin/python3
import json
"""Define a function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """convert from object to JSON(string)

    Args:
        my_obj: the object u wanna convert

    Return:
        JSON representation of an object (string)
    """
    return json.dumps(my_obj)
