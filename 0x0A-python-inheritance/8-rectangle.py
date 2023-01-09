#!/usr/bin/python3
"""
Contains the class BaseGemetry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The class empty"""

    def __init__(self, width, height):
        """raises an exception when called"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.heigth = height
