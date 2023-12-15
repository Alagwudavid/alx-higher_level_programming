#!/usr/bin/python3
"""Checks if object is an instance o a class"""


def is_same_class(obj, a_class):
    """Return true i object is an instance of the class, otherwise return false
    """
    return (type(obj) == a_class)
