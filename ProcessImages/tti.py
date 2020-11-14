#!/usr/bin/env python3
"""
Author   : Matthew Moore
Date     : 11/13/2020 
Revision : 11/13/2020
"""

from PIL import Image, ImageDraw
import sys

def main() -> None:
    if len(sys.argv) != 9:
        print('You must pass 8 arguments to this python file')
        quit(0)
        
    for i in range(1, 9, 2):
        img: Image = Image.new('RGB', (756, 100), "white")

        d: ImageDraw = ImageDraw.Draw(img)

        d.text((20, 20), sys.argv[i], fill=(0, 0, 0))

        img.save(f'{sys.argv[i + 1]}.png')

if __name__ == "__main__":
    main()