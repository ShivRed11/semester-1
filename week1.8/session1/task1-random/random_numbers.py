# Reference solution (rewritten after original work was lost)
import random

# Get user to input how many random numbers they want
how_many = int(input("How many random numbers do you want? "))

# Generate this many random numbers
numbers = []
for i in range(how_many):
    numbers.append(random.randint(1, 100))   # random integer from 1 to 100 inclusive

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as outfile:
    for number in numbers:
        outfile.write(f"{number}\n")   # write() needs a string, so use an f-string

print(f"Wrote {how_many} numbers to random.txt")
