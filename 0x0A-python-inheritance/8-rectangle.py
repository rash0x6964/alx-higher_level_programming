#!/usr/bin/python3
"""Define Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Instantiation.

        Args:
            width: the width of the rectangle
            height: the height of the rectangle

        Returns:
            Nothing

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
