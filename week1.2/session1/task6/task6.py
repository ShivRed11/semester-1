# Reference solution (rewritten after original work was lost)
# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    "Radiohead": ["Pablo Honey", "The Bends", "OK Computer"],
    "Arctic Monkeys": ["Whatever People Say I Am, That's What I'm Not", "Favourite Worst Nightmare", "AM"],
    "Taylor Swift": ["Fearless", "1989", "Folklore"]
}

# Pretty-print the data structure
# pprint lays nested data out neatly, one entry per line
pprint(music)

# Display details of one album recorded by a specific artist
# music["Radiohead"] gives the list, then [0] gives its first item
print(music["Radiohead"][0])

# Additional work 1: store album name AND year
# a tuple (name, year) suits this well: a fixed pair of related values
music_years = {
    "Radiohead": [("Pablo Honey", 1993), ("The Bends", 1995), ("OK Computer", 1997)],
    "Taylor Swift": [("Fearless", 2008), ("1989", 2014), ("Folklore", 2020)]
}
pprint(music_years)
print(music_years["Taylor Swift"][1][0])   # name of 2nd album
print(music_years["Taylor Swift"][1][1])   # year of 2nd album

# Additional work 2: count the total number of albums
# add up the length of each artist's album list
total = 0
for albums in music.values():
    total = total + len(albums)
print(f"Total albums: {total}")
