#!/usr/bin/python3
"""Define BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Class methods that raise an error.

        Returns:
            Nothing

        Raises:
            Exception: when u call this function.
        """
        raise Exception("area() is not implemented")
