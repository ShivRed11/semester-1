# Reference solution (rewritten after original work was lost)
# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

from geometry import Point, Circle

circle = Circle(5.0, Point(1.0, 1.0))
print(f"Circle: {circle}")

for p in [Point(1.0, 1.0), Point(4.0, 4.0), Point(6.0, 1.0), Point(5.0, 5.0)]:
    if p in circle:
        print(f"{p} is inside the circle")
    else:
        print(f"{p} is NOT inside the circle")

# Expected:
# (1.0, 1.0) inside (it's the centre)
# (4.0, 4.0) inside (distance 4.24)
# (6.0, 1.0) NOT inside (distance exactly 5, on the edge)
# (5.0, 5.0) NOT inside (distance 5.66)
