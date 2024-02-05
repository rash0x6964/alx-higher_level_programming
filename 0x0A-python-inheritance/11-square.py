#!/usr/bin/python3
"""Define Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Instantiation with size.

        Args:
            size: size of square

        Returns:
            Nothing
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Class methods that calc the area of this square.

        Returns:
            result of area
        """
        return self.__size * self.__size

    def __str__(self):
        """human-readable string representation of the object.

        Return:
            string ([Square] <width>/<height>)
        """
        return f"[{type(self).__name__}] {self.__size}/{self.__size}"
