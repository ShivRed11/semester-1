# Reference solution (rewritten after original work was lost)
# there are several errors in this code
# run the code, read the error messages or look at the output, and fix the problems

# Find and fix the errors
# Fixes made:
#   1. 'imput' was a typo -> input
#   2. int(age) = ... is not allowed (can't assign to a function call)
#      -> wrap the input() call in int() instead
#   3. 'city' line had an extra space at the start -> IndentationError, removed it
#   4. the print was missing the 'f' so {name} etc. were printed literally -> made it an f-string

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"Hello {name}, you are {age} years old and live in {city}.")
