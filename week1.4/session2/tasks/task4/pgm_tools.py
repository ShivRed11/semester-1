# Reference solution (rewritten after original work was lost)

# PGM functions that we write

def readPGM( filename ):
    ''' 
    Read a named PGM file and store the data in a tuple.
    Input: filename string
    Output: tuple of PGM image data
    '''

    with open(filename,"r") as f:    # read in the file
        data = f.readlines()

    # optional extra: drop any comment lines (they start with '#')
    data = [line for line in data if not line.startswith("#")]

    data = [line.strip().split() for line in data[1:]] # clean the space-separated data, skip the first line
          
    width = int(data[0][0]) # store the data - compare to the text in the file
    height = int(data[0][1])
    max_gray = int(data[1][0])
    pixels = [[int(data[2+i][j]) for j in range(width)] for i in range(height)] # nested list comprehension for pixel array
    
    return width,height,max_gray,pixels   # tuple of PGM data
    
def writePGM( filename, image ):
    '''
    Write a PGM file to disk
    Input: filename string, image tuple data
    Output: None
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    # open a file for writing
    # write the data in PGM format
    # don't forget the PGM code "P2"
    with open(filename, "w") as f:      # "w" creates/overwrites the file
        f.write("P2\n")                         # line 1: PGM code
        f.write(f"{width} {height}\n")          # line 2: width height
        f.write(f"{max_gray}\n")                # line 3: max gray value
        for row in pixels:                      # one line per row of pixels
            row_text = " ".join(str(value) for value in row)
            f.write(row_text + "\n")

    return

def invertPGM( image ):
    '''
    Invert an image, ie. pixel value = 255 - pixel value
    Input: image data
    Output: inverted image data
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    # your code
    # create a new pixel array of inverted data 
    # Note: the task says 255 - value, which is right for images whose
    # max_gray is 255. Using max_gray works for every image (feep.pgm has
    # max_gray 15, so 255 - value would give values above the maximum).
    inverted = [[max_gray - value for value in row] for row in pixels]
    
    return width,height,max_gray,inverted

def rotatePGM( image ):
    '''
    Rotate an image 90 degrees clockwise
    Input: image data
    Output: rotated image data (width and height swap over)
    '''
    width,height,max_gray,pixels = image

    # new row j is old column j, read from the bottom row up to the top
    rotated = [[pixels[height-1-i][j] for i in range(height)] for j in range(width)]

    return height,width,max_gray,rotated

def thresholdPGM( image, threshold ):
    '''
    Threshold an image: pixels below threshold become 0 (black),
    all others become max_gray (white)
    Input: image data, threshold value
    Output: thresholded image data
    '''
    width,height,max_gray,pixels = image

    result = [[0 if value < threshold else max_gray for value in row] for row in pixels]

    return width,height,max_gray,result

# code to test the PGM functions

image = readPGM("images/feep.pgm")

print(f"Image with width {image[0]} and height {image[1]}")
print(f"{image[3]}")

# write further code to test your own functions

# write the image straight back out - the new file should match the original
writePGM("feep_copy.pgm", image)
print(readPGM("feep_copy.pgm") == image)       # True

# invert, write to disk, then read back to check
inverted = invertPGM(image)
writePGM("feep_inverted.pgm", inverted)
print(readPGM("feep_inverted.pgm")[3])

# extra functions
rotated = rotatePGM(readPGM("images/plus.pgm"))
print(f"Rotated: width {rotated[0]}, height {rotated[1]}")
writePGM("feep_rotated.pgm", rotatePGM(image))
writePGM("feep_threshold.pgm", thresholdPGM(image, 8))

# the comment line is skipped, so this matches feep.pgm
print(readPGM("images/with_comment.pgm")[3] == image[3])   # True
