#!/usr/bin/python3
"""Build a Class"""


class Rectangle:
    """A class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """property to retrieve the value"""
        return self.__width

    @width.setter
    def width(self, value):
        """property to set the value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property to retrieve the value"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to set it"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """clac the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """clac the rectangle perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle with the character print_symbol"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        char = []
        for i in range(self.__height):
            char.append(str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                char.append("\n")
        return ("".join(char))

    def __repr__(self):
        """print the rectangle with repr function"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """print a message if an instance is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not all(isinstance(rect, Rectangle) for rect in [rect_1, rect_2]):
            raise TypeError("must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return Rectangle(size, size)
