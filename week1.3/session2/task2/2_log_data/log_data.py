# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.


# open and read the file
# NOTE: this assumes site.log is comma-separated, like the .csv files in this session
try:
    with open("site.log", "r") as f:
        data = f.readlines()
except FileNotFoundError:
    print("Error: site.log could not be found - make sure it is in the same folder.")
    data = []

# clean the data: remove the newline and split each line on the commas
# data[1:] skips the header row
rows = [line.strip().split(",") for line in data[1:]]

# find all failed login attempts (POST /login with the response 401)
# and print these out in a human-readable format:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20
# Key idea: each row is [Date, Time, IP_Address, User_Agent, Request, Status_Code]
# so Request is row[4] and Status_Code is row[5]. Both checks must be true -> use `and`.
failed = [row for row in rows if len(row) == 6 and row[4] == "POST /login" and row[5] == "401"]

for row in failed:
    date = row[0]
    time = row[1]
    ip = row[2]
    print(f"IP address {ip} failed to login at {time} on {date}")


# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data
