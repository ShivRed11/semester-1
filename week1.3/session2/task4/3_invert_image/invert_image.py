# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except
filename = input("Enter the image file name (e.g. ../images/feep.pgm): ")
output_filename = input("Enter the name for the inverted image (e.g. feep_inverted.pgm): ")

try:
    with open(filename, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Error: could not find {filename}")
    lines = []

# remove blank lines and comment lines, so the header is always lines[0] to lines[2]
lines = [line.strip() for line in lines if line.strip() != "" and not line.strip().startswith("#")]

if len(lines) >= 3:
    dimensions = lines[1].split()
    width = int(dimensions[0])
    height = int(dimensions[1])
    max_gray = int(lines[2])

    # Create inverted image
    # the formula: invert_pixel_value = max_gray - original_pixel_value
    # Key idea: black (0) becomes white (max_gray) and white becomes black.
    inverted_rows = []
    for line in lines[3:]:
        row = [max_gray - int(value) for value in line.split()]
        inverted_rows.append(row)


    # write the inverted pgm image to a new file.
    # Remember to include:
    # - the string `P2`
    # - the width and height dimensions
    # - maximum gray value
    # - you could convert numbers in a list to strings and join them with spaces
    #   for example line = [255, 255, 0, 255, 255]
    #   string_line = " ".join(str(item) for item in line)
    #   # output: string_line = "255 255 0 255 255"
    with open(output_filename, "w") as f:
        f.write("P2\n")
        f.write(f"{width} {height}\n")
        f.write(f"{max_gray}\n")
        for row in inverted_rows:
            string_line = " ".join(str(item) for item in row)
            f.write(string_line + "\n")

    print(f"Inverted image written to {output_filename}")
