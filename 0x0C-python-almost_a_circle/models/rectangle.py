#!/usr/bin/python3
"""Define a class Rectangle"""
from .base import Base


class Rectangle(Base):
    """A class that defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property to retrieve the value"""
        return self.__width

    @width.setter
    def width(self, value):
        """property to set the value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve the value"""
        return self.__height

    @height.setter
    def height(self, value):
        """property to set the value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property to retrieve the value"""
        return self.__x

    @x.setter
    def x(self, value):
        """property to set the value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property to retrieve the value"""
        return self.__y

    @y.setter
    def y(self, value):
        """property to set the value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """clac the rectangle area"""
        return (self.__width * self.__height)

    def display(self):
        """print the rectangle with the character #"""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """print the rectangle with format:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.

        Args:
            *args: A sequence of arguments
        """
        if args and len(args) != 0:
            attr = ["id", "width", "height", "x", "y"]
            for index, value in enumerate(args):
                setattr(self, attr[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Get the dictionary representation of a Rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
