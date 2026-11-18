# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 5a

course = "computer science"

# create a list data structure of the characters from the course string
characters = []

for ch in course:
	print(ch)
	characters.append(ch)    # add each character to the end of the list

print(characters)

# sort the list into alphabetical order
# .sort() sorts the list in place (the space ' ' sorts before the letters)
characters.sort()

print(characters)
