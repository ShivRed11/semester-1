# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# ask the user for the file name
filename = input("Enter the file name: ")

# open and read the file
# try/except stops the program crashing if the file name is wrong
try:
    with open(filename, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Sorry, the file {filename} could not be found.")
else:
    # calculate the number of words
    # hint: you could use .split() to break up by spaces
    # hint: watch out for empty lines that might give you empty strings
    # Key idea: line.split() with NO argument splits on any whitespace and ignores
    # extra spaces/newlines, so an empty line gives [] and adds 0 words.
    word_count = 0
    for line in lines:
        words = line.split()
        word_count = word_count + len(words)

    # display the wordcount
    print(f"{filename} contains {word_count} words.")

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210
