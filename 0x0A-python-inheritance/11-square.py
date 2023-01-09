#!/usr/bin/python3
"""
Contains the class BaseGemetry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The class empty"""

    def __init__(self, size):
        """A representation of a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        return (self.__size ** 2)
