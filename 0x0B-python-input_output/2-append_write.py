#!/usr/bin/python3
"""Module for append_write method.
"""


def append_write(filename="", text="") -> int:
    """Appends to a text file (UTF8).
    Args:
        filename (str): The name of the file to append.
        text (str): text to write to file.
    Returns:
        len (int): Number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
