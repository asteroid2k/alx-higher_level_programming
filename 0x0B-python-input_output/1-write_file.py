#!/usr/bin/python3
"""Module for write_file method.
"""


def write_file(filename="", text="") -> int:
    """Writes to a text file (UTF8).
    Args:
        filename (str): The name of the file to write.
        text (str): text to write to file.
    Returns:
        len (int): Number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
