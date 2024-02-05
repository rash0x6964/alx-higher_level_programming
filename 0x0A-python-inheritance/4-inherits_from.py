#!/usr/bin/python3
"""Define a function checkes the if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """function checks if the object is an instance of
        a class that inherited (directly or indirectly) from
        the specified class.

    Args:
        obj: the object we wanna check
        a_class: the target class

    Return:
        True if it's an instance of inherited class otherwise False
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
