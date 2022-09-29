#!/usr/bin/python3
"""Module for write_file method.
"""


def write_file(filename="", text=""):
    """Writes to a text file (UTF8).
    Args:
        filename (str): The name of the file to read.
        text (str): text to write to file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
