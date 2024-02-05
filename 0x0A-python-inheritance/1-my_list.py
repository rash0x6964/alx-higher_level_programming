#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        cpy = self.copy()
        cpy.sort()
        print(cpy)
