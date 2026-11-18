# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 1: Task 1a

i = 0

# Modify the loop to print numbers up to and including 20
# Key idea: use <= 20 (or < 21) so that 20 itself is included
while i <= 20:
	print(i)

	# Add further logic so that a message is printed if the number is a multiple of 4
	# Hint: we discused operators such as % and // in recent weeks
	# Key idea: i % 4 gives the remainder after dividing by 4 - if it is 0, i is a multiple of 4
	if i % 4 == 0:
		print(f"{i} is a multiple of 4")

	i = i + 1
