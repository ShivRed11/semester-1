# Reference solution (rewritten after original work was lost)
# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.


def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """

    # Key idea: walk through the list once, looking for the NEXT number we
    # need from the target sequence. Each time we find it, move on to the
    # following target number. If we get through all of 0, 0, 7 we are done.
    target = [0, 0, 7]
    position = 0                      # index of the next target number

    for number in intList:
        if number == target[position]:
            position += 1
            if position == len(target):   # found 0, 0 and 7 in order
                return True

    return False

# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 7, 5]))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False
print(isBond([0, 7, 0]))               # False (7 comes before 2nd 0)
