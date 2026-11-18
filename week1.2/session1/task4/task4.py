# Reference solution (rewritten after original work was lost)
# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
# intersection = items in BOTH sets -> {'tomato'}

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
# union = items in EITHER set; sets have no duplicates, so "tomato"
# only appears once: 3 + 3 - 1 = 5 items

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("banana")
print(fruit)

# Remove an item from vegetables
vegetables.remove("leek")
print(vegetables)

# Find and display symmetric difference of the two sets
# symmetric difference = items in one set OR the other, but NOT both
# (so "tomato" is left out)
different = fruit.symmetric_difference(vegetables)
print(different)
