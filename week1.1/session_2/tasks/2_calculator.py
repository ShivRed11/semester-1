# Reference solution (rewritten after original work was lost)
# Fill out the code to make a very simple calculator

# input() always returns a string, so we convert it with int() before doing maths

# ask the user to enter number1:
number1 = int(input("Enter number 1: "))

# ask the user to enter number 2:
number2 = int(input("Enter number 2: "))

# calculate the result of adding those numbers together
result = number1 + number2

# print out the answer
print(f"{number1} + {number2} = {result}")
