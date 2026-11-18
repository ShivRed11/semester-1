# Reference solution (rewritten after original work was lost)
# Week 1.7, Session 2: Task 1 - ValueError

# Run this program and observe what happens

# BUG (ValueError: too many values to unpack): looping over a dictionary
# directly gives only the KEYS (e.g. "username"), so Python tried to unpack
# the string "username" into two variables. FIX: use .items() to get
# (key, value) pairs.

user_profile = {"username": "alice99", "role": "admin"}

for key, value in user_profile.items():
    print(f"{key} : {value}")
