# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
try:
    with open("student_data.csv", "r") as f:
        data = f.readlines()
except FileNotFoundError:
    print("Error: student_data.csv could not be found.")
    data = []

# clean each line: remove the newline, then split on the commas
# data[1:] skips the header row (ID,Name,Mathematics,Science,History)
rows = [line.strip().split(",") for line in data[1:] if line.strip() != ""]


# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3
averages = []    # list of [name, average] pairs
for row in rows:
    name = row[1]
    maths = int(row[2])
    science = int(row[3])
    history = int(row[4])
    average = (maths + science + history) / 3
    averages.append([name, average])


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
with open("report.txt", "w") as f:
    f.write("Student Average Grades\n")
    for name, average in averages:
        f.write(f"{name}: {average:.2f}\n")

print(f"Report written to report.txt for {len(averages)} students")
