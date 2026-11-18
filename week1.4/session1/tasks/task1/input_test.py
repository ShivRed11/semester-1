# Reference solution (rewritten after original work was lost)

# Week 4, Session 1: Task 1 - the input() function
#
# Documentation (help(input) / docs.python.org):
#   input(prompt) - "Read a string from standard input. The trailing newline
#   is stripped."
#
# Inputs:  prompt (optional) - a string (any object, really) that is written
#          to the screen, without a trailing newline, before reading input.
# Output:  the line the user typed, ALWAYS returned as a str (type str),
#          with the trailing newline removed.
#
# Key idea: even if the user types a number, input() gives back a string,
# so we must convert it ourselves with int() or float() if we want a number.

name = input("What is your name? ")
print(f"Hello, {name}")
print(type(name))              # <class 'str'>

age_text = input("How old are you? ")
print(type(age_text))          # still <class 'str'>, even for "20"

age = int(age_text)            # convert the string to an integer
print(f"Next year you will be {age + 1}")
print(type(age))               # <class 'int'>

# The prompt is optional - this reads a line without printing anything first
print("Type anything:")
anything = input()
print(f"You typed '{anything}' which has {len(anything)} characters")
