# Reference solution (rewritten after original work was lost)
# See README.md for instructions on what to do this program

import random

random.seed(10)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

# What is happening:
# - random numbers in Python are "pseudo-random": they come from a formula that
#   starts from a starting value called the SEED.
# - With random.seed(10) the program prints the SAME three numbers every run,
#   because the formula always starts from the same place.
# - Changing the seed (e.g. random.seed(42)) gives a different set of numbers,
#   but again the same set every time you run it with that seed.
# - With the seed line commented out, Python seeds itself from the system
#   (e.g. the current time), so you get different numbers on every run.
# Fixing the seed is useful for testing/debugging, because results are repeatable.
