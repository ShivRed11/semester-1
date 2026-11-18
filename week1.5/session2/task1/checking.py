# Reference solution (rewritten after original work was lost)
# Week 1.5, Session 2: Task 1

# Add type checking to the constructor of Point

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        if not isinstance(x, (int,float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int,float)):
            raise TypeError("y is not a number")
        self.x = x
        self.y = y

    def distance(self):
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p):
        """
        Returns distance of this Point from the specified Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)


# Notes: isinstance(value, (int, float)) is True if value is an int OR a
# float. Anything else raises TypeError straight away, so the program now
# fails when the Point is CREATED, not later when distance() is called.

# Test program

p = Point("two", "one")
print(p.distance())
