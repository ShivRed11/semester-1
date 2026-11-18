# Reference solution (rewritten after original work was lost)
import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
how_many = int(input(f"How many names do you want to pick (1-{len(names)})? "))

# random.sample() picks items WITHOUT replacement, so no name is chosen twice.
# (random.choice() in a loop could pick the same name more than once.)
chosen = random.sample(names, how_many)

# Display the chosen names, one per line
for name in chosen:
    print(name)
