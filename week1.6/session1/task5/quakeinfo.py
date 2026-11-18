# Reference solution (rewritten after original work was lost)
# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like


x = 2
while x <= 10:
    print(x)
    x = x + 2



# ---------------------------------------------------------------------
# Reference solution for the task (the loop above is earlier work that
# was already in this file, and has been kept as it was)
# ---------------------------------------------------------------------

import sys

from dataset import QuakeDataset
from feed import QuakeFeed

# Level & period can be given on the command line, e.g.
#     python quakeinfo.py 4.5 week
# If they aren't, the user is prompted for them instead

if len(sys.argv) == 3:
    level = sys.argv[1]
    period = sys.argv[2]
else:
    level = input("Significance level (all, 1.0, 2.5, 4.5, significant): ")
    period = input("Time period (hour, day, week, month): ")

# QuakeFeed raises ValueError for an invalid level or period
try:
    feed = QuakeFeed(level, period)
except ValueError as error:
    sys.exit(f"Error: {error}")

dataset = QuakeDataset(feed)
dataset.read_feed()

if len(dataset) == 0:
    sys.exit(f"No quakes found in {feed}")

# print() uses QuakeDataset's __str__() method
print(dataset)
print(f"Mean depth = {dataset.mean_depth():.2f} km")
print(f"Mean magnitude = {dataset.mean_magnitude():.1f}")

quake = dataset.strongest_quake()

# quake.when is a datetime object, so we can format its parts separately
print()
print(f"Strongest quake occurred at {quake.when:%H:%M:%S} on {quake.when:%Y-%m-%d}")
print(f"at {quake.longitude}° longitude, {quake.latitude}° latitude")
print(f"The depth was {quake.depth} km")
print(f"The magnitude was {quake.magnitude}")
