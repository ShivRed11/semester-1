# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 3a

i = 0

while i < 20:
    i = i + 1

    # Add logic using continue so that multiples of 3 are not printed out
    # Key idea: i % 3 is 0 (falsy) for multiples of 3, and 1 or 2 (truthy) otherwise.
    # So `not i % 3` is True exactly when i is a multiple of 3.
    # continue skips the rest of this iteration and goes back to the top of the loop.
    if not i % 3:
        continue

    print(i)

# Note: i is increased BEFORE the continue, otherwise i would never change and
# the loop would run forever.
