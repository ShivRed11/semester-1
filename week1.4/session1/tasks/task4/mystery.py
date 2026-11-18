# Reference solution (rewritten after original work was lost)
# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type


# function implementation

def mystery_func(string):
    """
    Counts the uppercase and lowercase letters in a string.
    Characters that are not letters (digits, spaces, punctuation)
    are ignored.

    Args:
        string (str): The text to examine.

    Returns:
        tuple (int, int): (number of uppercase letters,
                           number of lowercase letters)
    """
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

# Predictions: "X" has one uppercase letter -> (1, 0)
# "[2, 3]" has no letters at all -> (0, 0)
print(mystery_func("X"))         # (1, 0)
print(mystery_func("[2, 3]"))    # (0, 0)
