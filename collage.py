#!/usr/bin/env python

"""
To collect picture in a grid

by WangLu
2011.03.04
"""

import Image
import math

INPUT_FILES = ['1.png','2.png','3.png','4.png','5.png','6.png']
OUTPUT_FILE = 'out.png'

NUMBER_OF_COLS = 3

BLOCK_WIDTH = 768
BLOCK_HEIGHT = 1024
MARGIN = 10
BACKGROUND_COLOR = (35,35,35)

def work():
    num_of_rows = int(math.ceil(float(len(INPUT_FILES)) / NUMBER_OF_COLS))
    out_width = NUMBER_OF_COLS * (BLOCK_WIDTH + MARGIN) + MARGIN
    out_height = num_of_rows * (BLOCK_HEIGHT + MARGIN) + MARGIN

    cur_col = 0
    cur_x = MARGIN
    cur_y = MARGIN

    out = Image.new("RGB", (out_width, out_height), BACKGROUND_COLOR)

    for f in INPUT_FILES:
        out.paste(Image.open(f), (cur_x, cur_y))
        cur_col += 1
        if cur_col < NUMBER_OF_COLS:
            cur_x += BLOCK_WIDTH + MARGIN
        else:
            cur_col = 0
            cur_x = MARGIN
            cur_y += BLOCK_HEIGHT + MARGIN
    out.save(OUTPUT_FILE)

if __name__ == '__main__':
    work()



