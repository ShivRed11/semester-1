# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
# .pop() removes AND returns the last item, so the list gets one item shorter on every pass.
#   1st iteration: fruit starts as ['apple','pear','banana','orange'] -> 'orange' is printed
#   4th iteration: fruit starts as ['apple'] -> 'apple' is printed
#   after the loop: fruit is [] (an empty list)
# Once the list is empty the condition is False, so the loop stops - it is not infinite.

# What features of Python does it rely on?
# - Truthiness: a non-empty list counts as True, an empty list counts as False,
#   so `while fruit:` means "while the list still has items in it".
# - The list method .pop(), which changes (mutates) the list in place.
