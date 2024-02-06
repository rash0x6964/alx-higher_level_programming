#!/usr/bin/python3
"""Define a function to wirte to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename: the name of the file
        text: the text u wanna write to the file

    Return:
        the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
