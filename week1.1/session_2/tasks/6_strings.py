# Reference solution (rewritten after original work was lost)
# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
# converts every letter to lowercase
print(f"Modified String 1: {user_string.lower()}")
# converts every letter to UPPERCASE
print(f"Modified String 2: {user_string.upper()}")
# removes spaces (whitespace) from the start and end
print(f"Modified String 3: {user_string.strip()}")
# replaces every 'a' with '@'
print(f"Modified String 4: {user_string.replace('a', '@')}")
# first character uppercase, the rest lowercase
print(f"Modified String 5: {user_string.capitalize()}")
# slicing with step -1 reverses the string
print(f"Modified String 6: {user_string[::-1]}")
# first letter of every word uppercase
print(f"Modified String 7: {user_string.title()}")
# number of characters in the string (its length)
print(f"Modified String 8: {len(user_string)}")
# index (position) of the first 'a', or -1 if not found
print(f"Modified String 9: {user_string.find('a')}")
# how many times 'a' appears
print(f"Modified String 10: {user_string.count('a')}")
# True if the string begins with 'Hello'
print(f"Modified String 11: {user_string.startswith('Hello')}")
# True if the string ends with '!'
print(f"Modified String 12: {user_string.endswith('!')}")
# True if all characters are letters or digits (no spaces/symbols)
print(f"Modified String 13: {user_string.isalnum()}")
# True if all characters are letters only
print(f"Modified String 14: {user_string.isalpha()}")
# True if all characters are digits only
print(f"Modified String 15: {user_string.isdigit()}")



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!

# Extras (from the w3schools string reference) and combining methods:
# swapcase() swaps upper and lower case
print(f"Extra 1: {user_string.swapcase()}")
# methods can be chained: strip the spaces, then make it uppercase
print(f"Extra 2: {user_string.strip().upper()}")
# count words by splitting on spaces and taking the length of the result
print(f"Extra 3: {len(user_string.split())}")
