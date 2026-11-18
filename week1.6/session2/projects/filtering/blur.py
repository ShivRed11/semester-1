# Reference solution (rewritten after original work was lost)
# Week 1.6, Session 2: Filtering project

# Program to blur a PGM image, e.g.
#     python blur.py original.pgm blurred.pgm

import sys

from filters import blur
from image import Image

if len(sys.argv) != 3:
    sys.exit("Usage: python blur.py <input-image> <output-image>")

original = Image.read(sys.argv[1])
blurred = blur(original)
blurred.write_pgm(sys.argv[2])

print(f"Blurred {sys.argv[1]} and wrote result to {sys.argv[2]}")
