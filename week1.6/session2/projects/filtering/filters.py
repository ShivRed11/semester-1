# Reference solution (rewritten after original work was lost)
# Week 1.6, Session 2: Filtering project

"""
Filtering operations for greyscale images.
"""

from image import Image


def blur(img):
    """
    Returns a new Image that is a 3x3 blurred version of the given Image.

    Edge pixels are left at 0, since a full 3x3 window doesn't fit there.
    """
    # Key idea: create a separate output image, so that the averages are
    # always computed from the ORIGINAL pixel values, not ones we've
    # already changed
    result = Image.create(img.width, img.height, maximum=img.max_value)

    # Loop limits skip the outermost rows & columns
    for row in range(1, img.height - 1):
        for col in range(1, img.width - 1):

            # Sum the 3x3 neighbourhood centred on (row, col)
            total = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    total += img.get(row + dr, col + dc)

            # Integer division keeps pixel values as whole numbers
            result.set(row, col, total // 9)

    return result
