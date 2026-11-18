# Reference solution (rewritten after original work was lost)
# Week 1.6, Session 2: Look-Up Tables project

"""
Look-up tables (LUTs) for transforming greyscale image pixel values.
"""

import math


class LookupTable:
    """
    A generic look-up table.

    The table is a list in which the value stored at index x is the new
    value to use for any pixel whose current value is x. This base class
    maps every value to itself (i.e., it leaves images unchanged).
    """

    def __init__(self, maximum=255):
        """
        Creates a LUT covering pixel values 0 to maximum.
        """
        self.maximum = maximum
        # Key idea: compute every possible result ONCE, up front, so that
        # processing an image is just a fast list lookup per pixel
        self.table = [self.function(x) for x in range(maximum + 1)]

    def function(self, x):
        """
        Returns the new value for pixel value x.

        Subclasses override this to define different transformations.
        """
        return x

    def __getitem__(self, value):
        """
        Returns the output value that the given pixel value maps to.
        """
        return self.table[value]

    def display(self):
        """
        Prints the mapping of pixel values performed by this LUT.
        """
        for value, result in enumerate(self.table):
            print(f"{value:3d} -> {result:3d}")

    def apply(self, img):
        """
        Returns a new Image produced by passing the given Image through this LUT.
        """
        result = img.copy()
        self.apply_in_place(result)
        return result

    def apply_in_place(self, img):
        """
        Modifies the given Image by passing its pixels through this LUT.
        """
        for i in range(img.width * img.height):
            img[i] = self[img[i]]


class InvertLUT(LookupTable):
    """
    A LUT that inverts brightness: white becomes black and vice versa.
    """

    def function(self, x):
        return self.maximum - x


class SqrtLUT(LookupTable):
    """
    A LUT that boosts contrast in dark areas and reduces it in bright ones.
    """

    def function(self, x):
        # Scale so that 0..maximum still maps onto 0..maximum
        scale = self.maximum / math.sqrt(self.maximum)
        return round(scale * math.sqrt(x))
