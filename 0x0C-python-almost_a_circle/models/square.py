#!/usr/bin/python3
"""Define a class Square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print the square with format:
            [Square] (<id>) <x>/<y> - <size>
        """
        return (
            f"[Square] ({self.id}) "
            f"{self.x}/{self.y} - "
            f"{self.width}"
        )

    @property
    def size(self):
        """property to retrieve the value"""
        return self.__size

    @size.setter
    def size(self, value):
        """property to set the value"""
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args: A sequence of arguments
        """
        if args and len(args) != 0:
            attr = ["id", "size", "x", "y"]
            for index, value in enumerate(args):
                setattr(self, attr[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Get the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
