# Reference solution (rewritten after original work was lost)
'''
This will combine some basic data handling, plotting, and writing functions.
You will probably want to have the docs/help open to support you!

The base code is provided at the bottom - you can add to this, change it, or remove it and write your own if you prefer!

You are welcome to add more options to the menu and create your own graphs - think of how you can use the different styles of graph.

For example - you could add box and whisker diagrams to show averages, or scatter plots to show outliers.

The data set 'ramen-ratings.csv' draws from a popular blog rating instant ramen products.
'''
import pandas as pd
import matplotlib.pyplot as plt
import random


def show_histogram_of_ramen_scores(data):
    '''
    Create a histogram to show the distribution of numbers of stars given to ramen.
    '''
    # bins = how many "buckets" the 0-5 star range is split into
    data["Stars"].plot(kind="hist", bins=20, title="Distribution of ramen star ratings")
    plt.xlabel("Stars")
    plt.ylabel("Number of ramen")
    plt.show()

def show_bar_chart_stars_per_manufacturer(data):
    '''
    Create a bar chart showing the average rating per manufacturer
    '''
    # group by Brand (the manufacturer) and take the mean of the Stars column
    averages = data.groupby("Brand")["Stars"].mean().sort_values(ascending=False)
    # there are hundreds of brands, so only plot the top 20 to keep it readable
    averages.head(20).plot(kind="bar", title="Average rating per manufacturer (top 20)")
    plt.xlabel("Manufacturer")
    plt.ylabel("Average stars")
    plt.tight_layout()   # stops long labels being cut off
    plt.show()

def show_bar_chart_stars_per_country(data):
    '''
    Create a bar chart showing the average rating per country
    '''
    averages = data.groupby("Country")["Stars"].mean().sort_values(ascending=False)
    averages.plot(kind="bar", title="Average rating per country")
    plt.xlabel("Country")
    plt.ylabel("Average stars")
    plt.tight_layout()
    plt.show()

def find_best_per_country(data, country):
    '''
    Find and return the index of the row with the highest rating per country.
    If there are two with equal rating, you can return either.
    '''
    # compare in lower case so "usa", "USA" and "Usa" all match (input uses .title())
    country_data = data[data["Country"].str.lower() == country.lower()]
    if country_data.empty:
        return None
    # idxmax() returns the INDEX (row label) of the largest value
    return country_data["Stars"].idxmax()

def find_worst_per_country(data, country):
    '''
    Find and return the index of the row with the lowest rating per country.
    '''
    country_data = data[data["Country"].str.lower() == country.lower()]
    if country_data.empty:
        return None
    return country_data["Stars"].idxmin()

def show_piechart_of_manufacturers_by_country(data, country):
    '''
    Create a pie chart showing the percentage of each manufacturer in the country
    '''
    country_data = data[data["Country"].str.lower() == country.lower()]
    if country_data.empty:
        print(f"No ramen found for {country}")
        return
    # value_counts() counts how many rows there are for each Brand
    brand_counts = country_data["Brand"].value_counts()
    brand_counts.plot(kind="pie", autopct="%1.1f%%", ylabel="",
                      title=f"Manufacturers of ramen from {country}")
    plt.show()

def print_ramen_rating(rating):
    '''
    Print out a row from the dataframe ('rating') in a more human-readable format, e.g.:

    Name: 
    Type of ramen:
    Manufacturer:
    Country of Origin:
    Stars:
    '''
    # 'rating' is one row (a Series), so we can index it by column name
    print(f"Name: {rating['Variety']}")
    print(f"Type of ramen: {rating['Style']}")
    print(f"Manufacturer: {rating['Brand']}")
    print(f"Country of Origin: {rating['Country']}")
    print(f"Stars: {rating['Stars']}")
    print()

def show_top_ten(data):
    '''
    Select the top-ten ramen and print them out in order of lowest rating to highest
    You may want to call your print_ramen_rating() function for this.
    '''
    # nlargest() picks the 10 highest-rated rows, then sort them low -> high
    top_ten = data.nlargest(10, "Stars").sort_values("Stars")
    # iterrows() gives (index, row) pairs, one per row
    for index, row in top_ten.iterrows():
        print_ramen_rating(row)

def random_ramen_review(data):
    '''
    Pick a random ramen from the dataframe and give it's basic information.
    You could also add:
        How it compares to its country and manufacturer averages
        A graph showing where it is on the histogram (you can add a vertical line at a specific value)
        Anything else you think would be interesting!
    '''
    # pick a random row label, then get that row with .loc[]
    index = random.choice(list(data.index))
    ramen = data.loc[index]
    print_ramen_rating(ramen)

    country_avg = data[data["Country"] == ramen["Country"]]["Stars"].mean()
    brand_avg = data[data["Brand"] == ramen["Brand"]]["Stars"].mean()
    print(f"Average for {ramen['Country']}: {country_avg:.2f} stars")
    print(f"Average for {ramen['Brand']}: {brand_avg:.2f} stars")

    # histogram of all scores, with a red line showing where this ramen sits
    data["Stars"].plot(kind="hist", bins=20, title="Where this ramen sits")
    plt.axvline(ramen["Stars"], color="red", label=ramen["Variety"])
    plt.xlabel("Stars")
    plt.legend()
    plt.show()


def menu():
    ''' Displays menu and allows user to enter choice to be returned to main - if you add more, remember to add them to the 'while choice not in' line! '''
    print("~ ramen rating database ~")
    print("1 - See distribution of scores")
    print("2 - see average score per country")
    print("3 - see average score per manufacturer")
    print("4 - Get a breakdown of a specific country")
    print("5 - See the top ten ramens")
    print("6 - See a random Ramen")
    choice = ""
    while choice not in ["1", "2", "3", "4", "5", "6", "Q"]:
        choice = input("Pick an option: ").upper()
    return choice

# the main program is below - complete the functions one at a time and test them!

ramen_data = pd.read_csv("ramen-ratings.csv")

# Cleaning: a few rows have "Unrated" in the Stars column, so pandas reads the
# whole column as text. to_numeric(errors="coerce") turns those into NaN (not
# a number), then dropna() removes them so mean/max etc. work properly.
ramen_data["Stars"] = pd.to_numeric(ramen_data["Stars"], errors="coerce")
ramen_data = ramen_data.dropna(subset=["Stars"])

while True:
    choice = menu()
    match choice:
        case "1":
            show_histogram_of_ramen_scores(ramen_data)
        case "2":
            # the template called the manufacturer function here, but the
            # menu says option 2 is "per country" - swapped to match the menu
            show_bar_chart_stars_per_country(ramen_data)
        case "3":
            show_bar_chart_stars_per_manufacturer(ramen_data)
        case "4":
            country = input("Enter country: ").title()
            best = find_best_per_country(ramen_data, country)
            worst = find_worst_per_country(ramen_data, country)
            if best is None:
                print(f"No ramen found for {country}")
            else:
                # the find functions return an index, so look the row up with .loc[]
                print("Best rated:")
                print_ramen_rating(ramen_data.loc[best])
                print("Worst rated:")
                print_ramen_rating(ramen_data.loc[worst])
                show_piechart_of_manufacturers_by_country(ramen_data, country)
        case "5":
            show_top_ten(ramen_data)
        case "6":
            random_ramen_review(ramen_data)
        case "Q":
            break
