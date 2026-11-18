# Reference solution (rewritten after original work was lost)
# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here


class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self):
        """
        Returns the distance of this Point from the origin (0, 0).
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance_to(self, other):
        """
        Returns the distance from this Point to another Point.
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)


# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle


class Circle:
    """
    A circle, represented by its radius and the Point at its centre.
    """

    def __init__(self, radius, centre=Point(0.0, 0.0)):
        """
        Creates a Circle, given a radius and (optionally) a centre Point.

        Radius comes first so that centre can have a default value:
        if centre is omitted the circle is centred on the origin.
        """
        self.radius = radius
        self.centre = centre      # a Circle "has a" Point (composition)

    def area(self):
        """
        Returns the area of this Circle (pi * r squared).
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Returns the perimeter (circumference) of this Circle (2 * pi * r).
        """
        return 2 * math.pi * self.radius


# Don't add any testing code to this file!
