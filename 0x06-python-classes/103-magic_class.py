#!/usr/bin/python3

import math

class MagicClass:
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(self.radius) is not float:
            raise TypeError("radius must be a number")
        else: self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius