# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 6b

values = [1,4,2,6,3,7]

print(values)

newval = []
for i in values:
    if i % 2 == 0:
        newval.append(2 * i)
    else:
        newval.append(i)

print(newval)

# write the list comprehension equivalent to the `for` loop
# Key idea: when there is an if AND an else, the conditional expression
# (value_if_true if condition else value_if_false) goes BEFORE the `for`.
newval_2 = [2 * i if i % 2 == 0 else i for i in values]

print(newval_2)
print(newval == newval_2)    # True
