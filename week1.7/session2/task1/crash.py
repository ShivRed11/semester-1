# Reference solution (rewritten after original work was lost)
# Week 1.7, Session 2: Task 1 - IndexError

# Run this program and observe what happens

# BUG (IndexError): the loop used range(100) but the list only has 10 items,
# so x[10] is out of range. FIX: loop over range(len(x)) so the loop always
# matches the size of the list.

def assign_values(x):
    for i in range(len(x)):
        x[i] = (i + 1) * (i + 1)

if __name__ == "__main__":
    data = [0] * 10
    assign_values(data)
    print(data)
    print("Done!")
