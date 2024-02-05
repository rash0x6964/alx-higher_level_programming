#!/usr/bin/python3
"""Define a function checkes the instance of a class or inherited from"""


def is_kind_of_class(obj, a_class):
    """function checks if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class

    Args:
        obj: the object we wanna check
        a_class: the target class

    Return:
        True if it's an instance of specified class otherwise False
    """
    return isinstance(obj, a_class)
