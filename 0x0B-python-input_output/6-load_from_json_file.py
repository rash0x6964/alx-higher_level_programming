#!/usr/bin/python3
"""Define a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file

    Args:
        filename: the name of the file

    Return:
        the created object
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
