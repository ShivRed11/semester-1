# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 4b



# create a for loop and use range to print the list of numbers 
# between 3 and 50 that are divisible by 3

# Key idea: start at 3 and step by 3, so every number produced is divisible by 3.
# The stop value 51 is not included, so the last number is 48.
numbers = []

for n in range(3, 51, 3):
    numbers.append(n)

print(numbers)

# Alternative: loop over every number and test it with %
# for n in range(3, 51):
#     if n % 3 == 0:
#         print(n)
