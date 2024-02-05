#!/usr/bin/python3
"""Define a function checkes the instance of a class"""


def is_same_class(obj, a_class):
    """function that check if the object is exactly an instance of the
        specified class

    Args:
        obj: the object we wanna check
        a_class: the target class

    Return:
        True if it's an instance of specified class otherwise False
    """
    return type(obj) is a_class
