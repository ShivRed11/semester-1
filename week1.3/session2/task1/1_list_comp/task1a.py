# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','hamster','goldfish']

not_fish = [item for item in animals if item != 'goldfish']

print(not_fish)


# write the equivalent for loop to create the not_fish list from animals
# Key idea: a list comprehension [item for item in animals if condition] is the same as
#   1. start with an empty list
#   2. loop over animals
#   3. if the condition is true, append the item itself (not a fixed string!)
not_fish_2 = []
for item in animals:
    if item != 'goldfish':
        not_fish_2.append(item)


# print your result to verify it is the same
print(not_fish_2)
print(not_fish == not_fish_2)    # True
