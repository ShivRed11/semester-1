# Reference solution (rewritten after original work was lost)
# Week 1.7, Session 2: Task 3

def calculate_total(price, tax_rate):
    print("Calculating total...")
    tax = price * tax_rate
    total = price + tax
    return total

item_price = 20     # FIX: was "20" (a string) -> TypeError when multiplied by 0.05
tax_percentage = 0.05

final_amount = calculate_total(item_price, tax_percentage)
print(f"Final Amount: {final_amount}")

# What was wrong: item_price was the string "20", not the number 20.
# In pdb, 'p price' showed '20' - the quotes prove it is a str.
# A string can't be multiplied by a float, so the fix is to remove the quotes.
# (Note: the header line above shifts the README's line numbers down by 1,
#  so the breakpoint from the README is now 'b 13' instead of 'b 12'.)
