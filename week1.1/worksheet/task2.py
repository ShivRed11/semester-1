"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Shiven Reddamoni 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
amount_input = input("Hi there. How much would you like to save every month?")
try:
    amount = int(amount_input)
    break
except not_integer:

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
total_amount = 12*amount
print(f"Your total mamount saved is {total_amount}")
# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
total_amount_intrest = total_amount * 1.008
print(f"Your total is total_amount_intrest")