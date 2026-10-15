# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers  

print("Put your decimals in")
decimals = read_numbers()
if len(decimals) == 0:
    sys.exit("Error: no numbers provided")

decimals.sort()

x = len(decimals)

min = min(decimals)
max = max(decimals)
mean = sum(decimals)/x
median = decimals[ x//2]

print(f"Minimum = {min}")
print(f"Maximum = {max}")
print(f"Mean = {mean}")
print(f"Median = {median}")







