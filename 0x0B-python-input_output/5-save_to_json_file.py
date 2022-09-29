#!/usr/bin/python3
"""Module save JSON representation of an object to file"""
import json


def save_to_json_file(my_obj: str, filename: str):
    """Function saves JSON representation of an object"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
