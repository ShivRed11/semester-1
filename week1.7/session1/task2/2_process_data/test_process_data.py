# Reference solution (rewritten after original work was lost)
# Week 1.7, Session 1: Task 2 - unit test for process_data() 

# Write test functions for the values you have chosen in the equivalence classes
# for testing the functions

# Hint: you should test for empty list, list with a single value, list with multiple values
# and for positive and negative integers


from process_data import process_data


def test_empty_list():
    # complete the implementation for
    # testing an empty list
    # Use "is None" (not "== None") to check for None
    assert process_data([]) is None
    
    
def test_one_int_list():
    # complete the implementation for 
    # testing a list with a single integer
    assert process_data([5]) == 5
    assert process_data([-5]) == -5
    assert process_data([0]) == 0      # sum is 0 but list is not empty


def test_multiple_int_list():
    # complete the implementation for
    # testing a list with multiple integers
    assert process_data([1, 2, 3]) == 6
    assert process_data([-1, -2, -3]) == -6
    assert process_data([-4, 10, 2]) == 8
    assert process_data([5, -5]) == 0
