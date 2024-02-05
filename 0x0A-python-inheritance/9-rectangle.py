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

    def area(self):
        """Class methods that calc the area of this rectangle.

        Returns:
            result of area
        """
        return self.__width * self.__height

    def __str__(self):
        """human-readable string representation of the object.

        Return:
            string ([Rectangle] <width>/<height>)
        """
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
