#!/usr/bin/python3
"""Define a class Square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print the square with format:
            [Square] (<id>) <x>/<y> - <size>
        """
        return (
            f"[Square] ({self.id}) "
            f"<{self.__x}>/<{self.__y}> - "
            f"<{self.__width}>"
        )
