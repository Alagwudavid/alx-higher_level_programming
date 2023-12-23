#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of this Rectangle instance.
        Returns:
            The width of this Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of this Rectangle instance.
        Args:
            value (int): The new width of this Rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of this Rectangle instance.
        Returns:
            The height of this Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of this Rectangle instance.
        Args:
            value (int): The new height of this Rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
