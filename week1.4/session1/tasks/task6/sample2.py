# Reference solution (rewritten after original work was lost)
# Week 4, Session 1: Task 3

# You are given function add_two_numbers. Your task is to inspect the code,
# and the run the program and observe the output.


def add_two_numbers(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return (num1 + num2)     # What happen if you remove the parenthesis ()?
    # Answer: nothing changes - return num1 + num2 works the same. The
    # brackets just group the expression; return is not a function.


# Check if the following lines produce the correct output
print(add_two_numbers(3, 4))
print(add_two_numbers(num1=3, num2=4))
print(add_two_numbers(3, num2=4))

# Why does the next line work?
# Answer: float("3") converts the STRING "3" to the number 3.0, so the
# function adds 3.0 + 4.0 = 7.0 (not string joining "34").
print(add_two_numbers("3", "4"))

# What happens if you try this? Uncomment the code to find out.
# print(add_two_numbers("three", "four"))
# Answer: it crashes with  ValueError: could not convert string to float:
# 'three'  - float() only understands strings that look like numbers.
# Keyword arguments (num1=3, num2=4) and mixing positional then keyword
# arguments all give 7.0, because each value still reaches the right
# parameter.
