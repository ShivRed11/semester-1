# Reference solution (rewritten after original work was lost)
# Week 1.5, Session 2: Task 1

# Add type hints to the Point class

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self) -> float:
        """
        Returns distance of this Point from the origin.
        """
        return math.hypot(self.x, self.y)

    def distance_to(self, p: "Point") -> float:
        """
        Returns distance of this Point from the specified Point.
        """
        return math.hypot(self.x - p.x, self.y - p.y)


# Notes:
# - 'float' also accepts int values when type checking.
# - "Point" is in quotes because the class isn't fully defined yet at
#   the point where distance_to() is written (a 'forward reference').
# - Hints don't change how Python runs the code: this still crashes in
#   distance(). But `mypy hinting.py` now reports that str is an
#   incompatible type for x and y on the line below.

# Test program

p = Point("two", "one")
print(p.distance())
