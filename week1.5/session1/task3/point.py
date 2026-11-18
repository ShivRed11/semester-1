# Reference solution (rewritten after original work was lost)
# Week 1.5, Session 1: Task 3

import math


class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        # self.x / self.y are FIELDS - they stay attached to the object
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self):
        """
        Returns the distance of this Point from the origin (0, 0).
        """
        # Pythagoras: hypotenuse of a triangle with sides x and y
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other):
        """
        Returns the distance from this Point to another Point.
        """
        # Same idea as distance(), but the triangle's sides are the
        # differences between the two points' coordinates
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)


# Finally, add code here to demonstrate use of Point

p = Point(3.0, 4.0)
print(f"x = {p.x}, y = {p.y}")                  # x = 3.0, y = 4.0
print(f"Distance from origin: {p.distance()}")  # 5.0

q = Point(6.0, 8.0)
print(f"Distance from p to q: {p.distance_to(q)}")   # 5.0
print(f"Distance from q to p: {q.distance_to(p)}")   # 5.0 (same both ways)
