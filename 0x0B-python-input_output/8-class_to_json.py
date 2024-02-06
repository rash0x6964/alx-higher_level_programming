#!/usr/bin/python3
"""Define a function that returns the dictionary description
    with simple data structure.
"""


def class_to_json(obj):
    """convert to a dictionary description
        with simple data structure.

    Args:
        obj: is an instance of a Class

    Return:
        dictionary
    """
    return obj.__dict__
