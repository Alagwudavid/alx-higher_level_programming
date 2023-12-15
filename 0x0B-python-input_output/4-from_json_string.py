#!/usr/bin/python3
"""
Write a function that returns an object "rom_json_string"
"""

import json


def from_json_string(my_str):
    """return the python data structure represented by a JSON string"""
    return json.loads(my_str)
