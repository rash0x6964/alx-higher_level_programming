#!/usr/bin/python3
"""Define a function that appends string to a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file

    Args:
        filename: name of the file
        text: the text u wanna appand

    Return:
        the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
