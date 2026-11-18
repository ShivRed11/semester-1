# Reference solution (rewritten after original work was lost)
# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
# index() returns the position of the first match (counting from 0)
position = fruit.index("banana")
print(f"banana is at position {position}")

# Display how many times "cherry" occurs
print(f"cherry occurs {fruit.count('cherry')} time(s)")

# Display how many times "strawberry" occurs
# count() returns 0 if the item isn't there (it doesn't cause an error)
print(f"strawberry occurs {fruit.count('strawberry')} time(s)")

# Unpack tuple into variables
# one variable per item, assigned in order
first, second, third = fruit
print(first)
print(second)
print(third)
