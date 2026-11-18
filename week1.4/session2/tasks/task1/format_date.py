# Reference solution (rewritten after original work was lost)
# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


# (The starter code called this format_data - renamed to format_date to
# match the instructions above.)
def format_date(day, month, year, separator="-"):
    # the f-string turns each number into text, with the separator between
    formatted_date = f"{day}{separator}{month}{separator}{year}"

    return formatted_date


# Write code to test the function with separators such as "/", ":", "."
print(format_date(25, 12, 2025))         # 25-12-2025 (default separator)
print(format_date(25, 12, 2025, "/"))    # 25/12/2025
print(format_date(25, 12, 2025, ":"))    # 25:12:2025
print(format_date(25, 12, 2025, separator="."))  # 25.12.2025
