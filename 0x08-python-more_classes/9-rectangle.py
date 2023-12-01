#!/usr/bin/python3
"""
Module that a defines a recctangle class
"""


class Rectangle:
    """
    Rectangle class

     Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
        number_of_instances (int): number of instances of the class
        print_symbol (any): symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
         Initializes a Rectangle instance
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width attribute
        Returns:
            width (int): width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute
        Args:
            value (int): value to set the width to
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute
        Returns:
            height (int): height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute
        Args:
            value (int): value to set the height to
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of the rectangle
        Returns:
            area (int): area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle
        Returns:
            perimeter (int): perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        Returns:
            str: string representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        return (str(self.print_symbol) * self.width + "\n") * self.height[:-1]

    def __repr__(self):
        """
        Returns a string representation of the rectangle instance
        Returns:
            str: string representation of the rectangle instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Deletes a Rectangle instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        Returns:
            Rectangle: the biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with width == height == size """

        return cls(size, size)
