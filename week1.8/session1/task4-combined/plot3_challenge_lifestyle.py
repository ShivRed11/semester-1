# Reference solution (rewritten after original work was lost)
'''
This is a difficult activity which will involve some relatively challenging filtering/sorting of data
You will want to have the docs or a guide on using matplotlib/pandas available, it is not expected that you do this completely independently.
chatGPT is very good when debugging Pandas, as it decodes error messages into more readable explanations- so if you are struggling to understand what 
you have done wrong I recommend pasting error messages into it!

All the basic program code has been included, you should be able to simply write the code to filter the data into an appropriate dataframe and then
plot and show the graphs.
'''

import pandas as pd
import matplotlib.pyplot as plt

# The 'hours per day' columns in lifestyle_data.csv - used by several functions
HOURS_COLUMNS = [
    "Study_Hours_Per_Day",
    "Extracurricular_Hours_Per_Day",
    "Sleep_Hours_Per_Day",
    "Social_Hours_Per_Day",
    "Physical_Activity_Hours_Per_Day",
]

def average_bar_chart(data):
    '''
    Complete this code to produce a bar chart of the total of each 'hours per day' column
    '''
    # The menu calls this "average hours per day", so we plot the mean of each
    # column (use .sum() instead of .mean() if you want the totals).
    averages = data[HOURS_COLUMNS].mean()
    averages.plot(kind="bar", title="Average hours per day for each activity")
    plt.xlabel("Activity")
    plt.ylabel("Hours per day")
    plt.tight_layout()
    plt.show()

def hours_histogram(data, column_name):
    '''
    Complete this code so that it can display a histogram of any given 'hours per day' column
    '''
    # check the user typed a real column name before trying to plot it
    if column_name not in HOURS_COLUMNS:
        print("Unknown column. Choose one of:")
        for col in HOURS_COLUMNS:
            print(" ", col)
        return
    data[column_name].plot(kind="hist", bins=20, title=f"Histogram of {column_name}")
    plt.xlabel("Hours per day")
    plt.ylabel("Number of students")
    plt.show()

def hours_pie_chart(data, student_id):
    '''
    Complete this code so that it produces a pie chart of any given student's hours per day - this should be selected by student ID (the first column)
    '''
    # Note: this copy of lifestyle_data.csv has no Student_ID column, so we
    # use the row number (the DataFrame index, starting at 0) as the ID.
    if student_id not in data.index:
        print(f"No student with ID {student_id}")
        return
    # .loc[row, columns] picks one student's row and just the hours columns
    student_hours = data.loc[student_id, HOURS_COLUMNS]
    student_hours.plot(kind="pie", autopct="%1.1f%%", ylabel="",
                       title=f"Hours per day for student {student_id}")
    plt.show()

def total_hours_per_stress_level(data, stress_level):
    '''
    Complete this code to create a stacked bar chart showing a breakdown of the total hours worked by students, grouped by their reported stress level.
    '''
    # groupby() makes one row per stress level; sum() totals each hours column
    totals = data.groupby("Stress_Level")[HOURS_COLUMNS].sum()
    print(totals)

    # if the user entered a valid level (e.g. "High"), show just that bar;
    # otherwise show all the levels side by side
    if stress_level in totals.index:
        totals = totals.loc[[stress_level]]   # double [] keeps it as a DataFrame
    else:
        print(f"'{stress_level}' not found - showing all stress levels")

    # stacked=True puts each activity on top of the previous one in one bar
    totals.plot(kind="bar", stacked=True, title="Total hours by stress level")
    plt.xlabel("Stress level")
    plt.ylabel("Total hours per day (all students)")
    plt.tight_layout()
    plt.show()

def display_menu():
    print("Student Lifestyle Data Analysis")
    print("1 - view average hours per day")
    print("2 - view specific activity")
    print("3 - view per-student breakdown")
    print("4 - view per stress level breakdown")
    print("Q - quit")
    choice = 0
    while choice not in ["1","2","3","4","Q"]:
        choice = input("Select option: ").upper()
    return choice


## main program:

data = pd.read_csv("lifestyle_data.csv")

# Note - when you run this in Interactive mode, the 'input' will be through a pop up instead of the terminal.
while True:
    choice = display_menu()
    match choice:
        case "Q":
            break
        case "1":
            average_bar_chart(data)
        case "2":
            col = input("Enter Hours Per column to analyse: ")
            hours_histogram(data, col)
        case "3":
            stid = int(input("Enter student ID: "))
            hours_pie_chart(data, stid)
        case "4":
            stress_level = input("Enter stress level: ").title()
            total_hours_per_stress_level(data, stress_level)
