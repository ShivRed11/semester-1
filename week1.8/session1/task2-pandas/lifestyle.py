# Reference solution (rewritten after original work was lost)
import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
# Answer: a pandas DataFrame (a table of rows and named columns).
# A single column, e.g. data["GPA"], is a pandas Series.
print(type(data))
print(data.head())       # check the first 5 rows look sensible

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
# (each row is one student; len(data) or data.shape[0] both work.
#  data.describe() also shows a 'count' row for each numeric column)
print("Number of students:", len(data))

# Find the mean average GPA of the students
print("Mean GPA:", data["GPA"].mean())

# Find the standard deviation of how much sleep students get per day
print("Std dev of sleep hours:", data["Sleep_Hours_Per_Day"].std())

# Find the maximum amount of study hours per day
print("Max study hours:", data["Study_Hours_Per_Day"].max())

# Sort the students by social hours per day ascending (lowest -> highest)
# sort_values() returns a NEW DataFrame - it doesn't change 'data'
sorted_by_social = data.sort_values("Social_Hours_Per_Day")
print(sorted_by_social.head())

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
hours_columns = [
    "Study_Hours_Per_Day",
    "Extracurricular_Hours_Per_Day",
    "Sleep_Hours_Per_Day",
    "Social_Hours_Per_Day",
    "Physical_Activity_Hours_Per_Day",
]
# sum(axis=1) adds ACROSS each row (axis=0 would add down each column)
data["Total_hours"] = data[hours_columns].sum(axis=1)
print(data.head())

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
# A boolean "mask" (True/False for each row) is used inside [] to filter rows.
# Note: the values in the file are capitalised ("High", "Low", "Moderate").
high_stress = data[data["Stress_Level"] == "High"]
low_stress = data[data["Stress_Level"] == "Low"]

print("High stress students:", len(high_stress), "mean GPA:", high_stress["GPA"].mean())
print("Low stress students:", len(low_stress), "mean GPA:", low_stress["GPA"].mean())

if high_stress["GPA"].mean() > low_stress["GPA"].mean():
    print("On average, high-stress students have a higher GPA in this data.")
else:
    print("On average, high-stress students do NOT have a higher GPA in this data.")
# Note: this only shows a link (correlation), not that stress CAUSES a higher GPA.
# e.g. students who study more may be both more stressed and get higher grades.
