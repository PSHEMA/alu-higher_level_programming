#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """Creates a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Prints the rectangle with #"""

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for i in range(self.__height):
            rectangle += (str(self.print_symbol) * self.__width)

            if i != (self.__height - 1):
                rectangle += "\n"

        return rectangle

    def __repr__(self):
        """Returns a string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""

        return cls(size, size)
