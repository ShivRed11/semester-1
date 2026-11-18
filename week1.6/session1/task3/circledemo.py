# Reference solution (rewritten after original work was lost)
# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

from point import Point
from shapes import Circle

# Colour not given, so the default of "red" is used
circle = Circle(2.5, Point(0.0, 0.0))
print(circle)    # print() calls Circle's __str__() method

print(f"Area = {circle.area():.3f}")
print(f"Perimeter = {circle.perimeter():.3f}")

# set_position() and set_colour() aren't defined in Circle -
# they are inherited from Shape
print("Moving the circle...")
circle.set_position(Point(1.6, 3.2))
print(circle)

print("Changing the circle's colour...")
circle.set_colour("green")
print(circle)
