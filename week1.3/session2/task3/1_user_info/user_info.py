# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
name = input("What is your name? ")
age = input("What is your age? ")
favourite_colour = input("What is your favourite colour? ")

# Open a file called 'user_info.txt' for writing
# Key idea: the mode 'w' opens the file for WRITING (it creates the file, or empties it
# if it already exists). The default mode 'r' is read-only, so writing would fail.
with open("user_info.txt", "w") as f:

    # Write each piece of information to the file, each on a new line.
    # Hints:
    # - Remember to add \n for new lines when writing to files
    # (.write() does not add a newline for you, unlike print())
    f.write(name + "\n")
    f.write(age + "\n")
    f.write(favourite_colour + "\n")

print("Your information has been saved to user_info.txt")


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
# Mode 'a' adds to the END of the file instead of wiping it.
while True:
    another = input("Add another person? (y/n) ")
    if another != "y":
        break

    name = input("What is your name? ")
    age = input("What is your age? ")
    favourite_colour = input("What is your favourite colour? ")

    with open("user_info.txt", "a") as f:
        f.write(name + "\n")
        f.write(age + "\n")
        f.write(favourite_colour + "\n")

    print("Saved!")
