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

    def integer_validator(self, name, value):
        """Class methods that validates value.

        Args:
            name: name of the value
            value: an integer

        Returns:
            Nothing

        Raises:
            TypeError: if value not integer
            ValueError: if value less or equal 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
