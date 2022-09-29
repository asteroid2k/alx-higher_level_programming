#!/usr/bin/python3

"""Module creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """Create object from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
