# Reference solution (rewritten after original work was lost)

import matplotlib.pyplot as plt  # import library

x = [ k for k in range(10) ]  # create a range for the data
y = [ k*k for k in x ]      # create a simple function y=x^2

plt.plot(x,y)  # create a 2d plot

plt.xlabel('x')
plt.ylabel('y=x^2')  # annotate

plt.show()  # display

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions


# --- Modified data and range: -10 to 10, with two functions on one graph ---
x = [ k for k in range(-10, 11) ]
y_square = [ k*k for k in x ]
y_cube = [ k*k*k / 10 for k in x ]

# marker= draws a dot at each data point, label= is used by the legend
plt.plot(x, y_square, marker='o', color='blue', label='y = x^2')
plt.plot(x, y_cube, linestyle='--', color='red', label='y = x^3 / 10')

# --- Annotation ---
plt.title('Square and cube functions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
# annotate() puts text on the plot, with an arrow pointing to a data point
plt.annotate('minimum of x^2', xy=(0, 0), xytext=(2, 60),
             arrowprops={'arrowstyle': '->'})

plt.show()


# --- Other ways of plotting the same data ---
# bar chart
plt.bar(x, y_square, color='green')
plt.title('Bar chart of y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# scatter plot (points only, no joining lines)
plt.scatter(x, y_cube, color='purple')
plt.title('Scatter plot of y = x^3 / 10')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
