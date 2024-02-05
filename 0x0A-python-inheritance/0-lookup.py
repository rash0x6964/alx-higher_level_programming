#!/usr/bin/python3
"""Define a lookup function"""


def lookup(obj):
    """Get the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of attributes and methods.

    """
    return dir(obj)
