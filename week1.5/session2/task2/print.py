# Reference solution (rewritten after original work was lost)
# Week 1.5, Session 2: Task 2

# Write code here to create and print a Point object,
# then create and print a Circle object

from geometry import Point, Circle

p = Point(3.0, 4.0)
print(p)        # (3.0, 4.0)  - without __str__ it was <geometry.Point object at 0x...>

c = Circle(2.5, Point(1.0, -1.0))
print(c)        # Circle with radius 2.5, centred at (1.0, -1.0)

print(Circle(1.0))   # default centre: Circle with radius 1.0, centred at (0.0, 0.0)
