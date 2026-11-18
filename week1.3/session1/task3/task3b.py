# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 3b

fruit = ['apple','pear','banana','orange']

while fruit:
	print(fruit.pop())

# Add an else clause with a message that the list is now empty
# Key idea: a while loop's else block runs when the condition becomes False
# (it would NOT run if the loop was exited with break).
else:
	print("The list is now empty")
