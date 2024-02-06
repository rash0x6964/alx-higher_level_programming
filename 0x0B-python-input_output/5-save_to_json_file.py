#!/usr/bin/python3
"""Define a function that writes an Object to a text file,
    using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file

    Args:
        my_obj: the object u wanna save
        filename: the name of the file

    Return:
        Nothing
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
