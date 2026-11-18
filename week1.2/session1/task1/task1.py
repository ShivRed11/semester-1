# Reference solution (rewritten after original work was lost)
# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes
# lists are indexed from 0: after removing "eggs" the list is
# ["milk", "flour", "carrots", "bananas"], so bananas is at index 3
shopping[3] = "grapes"
print(shopping)

# Add yoghurt, just after milk
# milk is at index 0, so insert() at index 1 puts yoghurt right after it
shopping.insert(1, "yoghurt")
print(shopping)
