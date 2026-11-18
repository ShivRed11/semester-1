# Reference solution (rewritten after original work was lost)
# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum

from money import Money

a = Money(1, 99)
b = Money(0, 5)
print(a)            # £1.99
print(b)            # £0.05

total = a + b       # the + operator calls a.__add__(b)
print(total)        # £2.04

print(Money(150, 0) + Money(17, 99))   # £167.99
