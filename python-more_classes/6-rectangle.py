#!/usr/bin/python3
"""A class Rectangle thst defines a rectangle"""


class Rectangle:
    """
    Defines a rectangle by its width and height
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance
        Args:
            width (int): width of the rectangle (default: 0)
            height (int): height of the rectangle (default: 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """
        Returns a string representation of the Rectangle instance
        that can be used to recreate the instance using eval()
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a message when a Rectangle instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Gets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args:
            value (int): the width of the rectangle
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        Args:
            value (int): the height of the rectangle
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns:
            The perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
