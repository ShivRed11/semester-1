# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 2a

# As written this is an infinite loop.
# If you run it, use <Ctrl>C to exit the running program.

# 1. Add a break statement to exit the loop if k>200
k = 2
while True:
    k = 2 * k 
    print(k)
    if k > 200:
        break    # break jumps straight out of the loop

print("---")

# 2. Rewrite the code to directly use the while loop instead of break.
# Key idea: put the stopping test in the while condition instead.
# The loop keeps going while k <= 200 (the opposite of the break condition k > 200).
k = 2
while k <= 200:
    k = 2 * k 
    print(k)

# Both versions print 4, 8, 16, 32, 64, 128, 256
