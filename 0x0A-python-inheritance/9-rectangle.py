#!/usr/bin/python3
"""
contains the class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle, inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of a rectangle
        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
