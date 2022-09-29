#!/usr/bin/python3
"""Module returns object from JSON representation"""
import json


def from_json_string(my_obj) -> str:
    """Function returns JSON representation of an object"""
    return json.loads(my_obj)
