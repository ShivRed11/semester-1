# Reference solution (rewritten after original work was lost)

# Week 4, Session 1: Task 3
# A function that accepts an integer value and returns a list of the
# even integers between 0 and that value (inclusive).

def even_numbers(limit):
    # range(start, stop, step): step 2 from 0 gives only even numbers.
    # stop is limit + 1 so that limit itself is included if it is even.
    evens = list(range(0, limit + 1, 2))
    return evens


# testing the function

print(even_numbers(10))   # [0, 2, 4, 6, 8, 10]
print(even_numbers(7))    # [0, 2, 4, 6]
print(even_numbers(0))    # [0]
