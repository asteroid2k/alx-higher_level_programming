#!/usr/bin/python3
"""Module returns JSON representation of an object"""
import json


def to_json_string(my_obj) -> str:
    """Function returns JSON representation of an object"""
    return json.dumps(my_obj)
