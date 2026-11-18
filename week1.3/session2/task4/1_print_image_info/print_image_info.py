# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.
filename = input("Enter the image file name (e.g. ../images/feep.pgm): ")

try:
    with open(filename, "r") as f:
        # Read the file content
        lines = f.readlines()
except FileNotFoundError:
    print(f"Error: could not find {filename}")
    lines = []

# Key idea: clean each line, and throw away blank lines and comment lines (starting with #).
# What is left is always in the same order:
#   lines[0] -> "P2"
#   lines[1] -> "width height"
#   lines[2] -> max gray value
#   lines[3:] -> the rows of pixels
lines = [line.strip() for line in lines if line.strip() != "" and not line.strip().startswith("#")]

if len(lines) >= 3:
    dimensions = lines[1].split()
    width = int(dimensions[0])
    height = int(dimensions[1])
    max_gray = int(lines[2])

    # print image dimension (i.e., Dimensions: width x height pixels)
    print(f"Dimensions: {width} x {height} pixels")

    # print max gray value (i.e., Max Gray Value: max_gray_value)
    print(f"Max Gray Value: {max_gray}")
