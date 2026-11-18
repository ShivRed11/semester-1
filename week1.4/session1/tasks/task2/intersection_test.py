# Reference solution (rewritten after original work was lost)

# Week 4, Session 1: Task 2 - the set.intersection() method
#
# Documentation (help(set.intersection) / docs.python.org):
#   set.intersection(*others) - "Return a new set with elements common to
#   the set and all others."
#
# Inputs:  zero or more "others" - any iterables (sets, lists, tuples,
#          strings...). It is called ON a set: s.intersection(...)
# Output:  a NEW set (type set) containing only the items found in the
#          original set AND in every one of the others.
#          The original set is NOT changed.
#
# The & operator does the same thing, but both sides must be sets.

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}
set_c = {5, 7, 9}

common = set_a.intersection(set_b)
print(common)                   # {4, 5}
print(type(common))             # <class 'set'>
print(set_a)                    # unchanged: {1, 2, 3, 4, 5}

# more than one argument - items common to all three sets
print(set_a.intersection(set_b, set_c))   # {5}

# the argument can be any iterable, e.g. a list
print(set_a.intersection([2, 4, 6, 8]))   # {2, 4}

# nothing in common gives an empty set
print(set_a.intersection({10, 11}))       # set()

# with no arguments you just get a copy of the set
print(set_a.intersection())               # {1, 2, 3, 4, 5}

# operator version
print(set_a & set_b)                      # {4, 5}
