#!/usr/bin/python3
"""Define function to read from file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename: the name of the file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
