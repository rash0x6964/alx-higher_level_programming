#!/usr/bin/python3
''' define a class Square'''


class Square():
    ''' the class square '''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a new square.'''
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2\
        or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        x, y = self.__position
        if self.__size == 0:
            print()
            return
        print("\n" * y, end='')
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
