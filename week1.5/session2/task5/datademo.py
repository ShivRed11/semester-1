# Reference solution (rewritten after original work was lost)
# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)

# Only the Dataset API is used here (len, mean, median, for loop) -
# never dataset.data directly.

from data import Dataset

filename = input("Enter name of data file: ")
dataset = Dataset(filename)

print(f"Size of dataset: {len(dataset)}")
print(f"Mean: {dataset.mean():.3f}")
print(f"Median: {dataset.median()}")

print("Values:")
for value in dataset:
    print(value)

# A data file just needs one number per line, e.g. a file values.txt:
# 4
# 8
# 15
# 16
# 23
# 42
