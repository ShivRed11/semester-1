# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except
filename = input("Enter the image file name (e.g. ../images/plus.pgm): ")

try:
    with open(filename, "r") as f:
        # Read the file content
        lines = f.readlines()
except FileNotFoundError:
    print(f"Error: could not find {filename}")
    lines = []

# remove blank lines and comment lines, so the header is always lines[0] to lines[2]
lines = [line.strip() for line in lines if line.strip() != "" and not line.strip().startswith("#")]

if len(lines) >= 3:
    # Store the width, the height, and the maximum gray value
    dimensions = lines[1].split()
    width = int(dimensions[0])
    height = int(dimensions[1])
    max_gray = int(lines[2])

    # turn each row of pixels into a list of ints, e.g. "255 0 255" -> [255, 0, 255]
    pixel_rows = []
    for line in lines[3:]:
        row = [int(value) for value in line.split()]
        pixel_rows.append(row)

    # For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive
    pixels_ok = True
    for row in pixel_rows:
        for pixel in row:
            if pixel < 0 or pixel > max_gray:
                pixels_ok = False

    # Check if the widths and heights are the same as specified
    # width: every row must have exactly `width` pixels
    width_ok = True
    for row in pixel_rows:
        if len(row) != width:
            width_ok = False

    # height: there must be exactly `height` rows
    height_ok = len(pixel_rows) == height

    # 4. Print the final verdit.
    #  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
    #  Print `Invalid width` if the widths are different
    #  Print `Invalid height` if the heights are different
    #  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value
    if width_ok and height_ok and pixels_ok:
        print("Valid image")
    else:
        if not width_ok:
            print("Invalid width")
        if not height_ok:
            print("Invalid height")
        if not pixels_ok:
            print("Invalid pixel values")
