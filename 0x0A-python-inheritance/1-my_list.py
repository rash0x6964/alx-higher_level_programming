#!/usr/bin/python3

"""Define a class inherits from list class"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """Class methods that prints the list, but sorted.

        Returns:
            Nothing

        """
        cpy = self.copy()
        cpy.sort()
        print(cpy)
