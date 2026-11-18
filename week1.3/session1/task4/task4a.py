# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 4a

# Original starter code (sums the squares of 1 to 9):
# sum = 0
# for k in range(1,10):
#     sum = sum + k ** 2
# print(sum)


# modify the code to sum the squares of even numbers up to and including 20
# Key idea: range(start, stop, step) - start at 2, step by 2, and stop at 21
# because the stop value itself is NOT included.
sum = 0

for k in range(2, 21, 2):
    sum = sum + k ** 2

print(sum)    # 1540

print("---")

# modify the code to print the sum at each iteration
# Key idea: move print() inside the loop (indent it) so it runs every time round.
sum = 0

for k in range(2, 21, 2):
    sum = sum + k ** 2
    print(sum)
