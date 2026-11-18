# Reference solution (rewritten after original work was lost)

# Week 4, Session 1: Task 3
# A function that accepts a list of integers and returns the mean average.

def mean_average(numbers):
    # mean = total of the values / how many values there are
    # guard against an empty list, which would divide by zero
    if len(numbers) == 0:
        return None
    mean = sum(numbers) / len(numbers)
    return mean


# testing the function

print(mean_average([1, 2, 3, 4, 5]))   # 3.0
print(mean_average([10, 15]))          # 12.5
print(mean_average([]))                # None
