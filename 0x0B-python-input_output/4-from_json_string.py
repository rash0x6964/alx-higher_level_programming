#!/usr/bin/python3
import json
"""Define a function that returns an object
    (Python data structure) represented by a JSON string
"""


def from_json_string(my_str):
    """Convert JSON string to an object

    Args:
        my_str: the JSON string u wanna convert

    Return:
        an Object (python data structure)
    """
    return json.loads(my_str)
