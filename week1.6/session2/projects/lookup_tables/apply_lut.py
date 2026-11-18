# Reference solution (rewritten after original work was lost)
# Week 1.6, Session 2: Look-Up Tables project

# Program to apply a LUT to a PGM image, e.g.
#     python apply_lut.py invert original.pgm result.pgm
#     python apply_lut.py sqrt original.pgm result.pgm

import sys

from image import Image
from lut import InvertLUT, SqrtLUT

LUT_TYPES = {"invert": InvertLUT, "sqrt": SqrtLUT}

if len(sys.argv) != 4 or sys.argv[1] not in LUT_TYPES:
    sys.exit("Usage: python apply_lut.py invert|sqrt <input-image> <output-image>")

img = Image.read(sys.argv[2])

# Build the LUT to suit this image's range of pixel values
lut_class = LUT_TYPES[sys.argv[1]]
lut = lut_class(img.max_value)

# Small tables are easy to inspect, so show the mapping for those
if img.max_value < 20:
    lut.display()

result = lut.apply(img)
result.write_pgm(sys.argv[3])

print(f"Applied {sys.argv[1]} LUT to {sys.argv[2]}, wrote {sys.argv[3]}")
