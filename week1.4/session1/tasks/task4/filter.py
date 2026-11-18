# Reference solution (rewritten after original work was lost)
# Week 4, Session 1: 

# Your are given the function filter_positive_numbers with a docstring.
# Can you identify the inconsistency between the docstring and the implementation?

# Your task is to update the docstring to reflect what the function does.


def filter_positive_numbers(numbers):
    # Inconsistency: the old first line said it keeps only the NEGATIVE
    # numbers, but the comprehension keeps num > 0, i.e. the POSITIVE ones.
    # (Zero is not positive, so 0 is dropped as well as negatives.)
    """
    Filters the list, keeping only the positive numbers (greater than 0).
    Negative numbers and zero are removed. The input list is not changed;
    a new list of all the positive numbers in the input is returned.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        list of int: A list containing only the positive integers.
    """
    return [num for num in numbers if num > 0]


# testing
print(filter_positive_numbers([3, -1, 0, 7, -5]))   # [3, 7]
