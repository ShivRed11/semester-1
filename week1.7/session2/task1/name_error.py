# Reference solution (rewritten after original work was lost)
# Week 1.7, Session 2: Task 1 - NameError

# Run this program and observe what happens

# BUG (NameError): 'total' was used (total = total + amount) before it had
# ever been given a value. FIX: create the variable with a starting value
# of 0 before the loop.

expenses = [10, 20, 30]

total = 0
for amount in expenses:
    total = total + amount  

print(total)
