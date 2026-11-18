# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
try:
    with open("sales.csv", "r") as f:
        data = f.readlines()
except FileNotFoundError:
    print("Error: sales.csv could not be found.")
    data = []

# clean the data and skip the header row
# each row becomes [Date, Product, Sales_Amount, Units_Sold, Region]
rows = [line.strip().split(",") for line in data[1:] if line.strip() != ""]

if len(rows) > 0:

    # find the:
    #   - largest sale day (highest sale amount)
    # Key idea: remember the best row seen so far and replace it if we find a bigger one
    best_row = rows[0]
    for row in rows:
        if int(row[2]) > int(best_row[2]):
            best_row = row

    #   - average sale amount
    total_sales = 0
    for row in rows:
        total_sales = total_sales + int(row[2])
    average_sale = total_sales / len(rows)

    #   - the widget which has been sold the most
    # Key idea: use a dictionary to add up the units sold for each product
    units_per_product = {}
    for row in rows:
        product = row[1]
        units = int(row[3])
        if product in units_per_product:
            units_per_product[product] = units_per_product[product] + units
        else:
            units_per_product[product] = units

    top_product = ""
    top_units = 0
    for product, units in units_per_product.items():
        if units > top_units:
            top_product = product
            top_units = units

    # and print these out in a nice, human-readable format
    print("Sales Summary")
    print("-------------")
    print(f"Largest sale day: {best_row[0]} ({best_row[1]}, £{int(best_row[2])})")
    print(f"Average sale amount: £{average_sale:.2f}")
    print(f"Most sold widget: {top_product} ({top_units} units)")


    # additional: you can calculate other sales statistics such as:
    # - total sales for each region
    # - most sold widget for each region
    # - total sales for each widget
    # Same dictionary pattern as above, just using a different column as the key.
    # .get(key, 0) returns 0 if the key is not in the dictionary yet (a shortcut for the if/else above)
    sales_per_region = {}
    for row in rows:
        region = row[4]
        sales_per_region[region] = sales_per_region.get(region, 0) + int(row[2])

    sales_per_product = {}
    for row in rows:
        product = row[1]
        sales_per_product[product] = sales_per_product.get(product, 0) + int(row[2])

    print()
    print("Total sales for each region:")
    for region, amount in sales_per_region.items():
        print(f"  {region}: £{amount}")

    print("Total sales for each widget:")
    for product, amount in sales_per_product.items():
        print(f"  {product}: £{amount}")


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows
