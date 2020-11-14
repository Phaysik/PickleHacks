#!/usr/bin/env python3
"""
Author   : Matthew Moore
Date     : 11/13/2020 
Revision : 11/13/2020
"""

from PIL import Image, ImageDraw

def main() -> None:
    img: Image = Image.new('RGB', (756, 100), "white")
    
    d: ImageDraw = ImageDraw.Draw(img)
    
    d.text((20, 20), 'bkonichiwa', fill=(0, 0, 0))
    
    img.save('rhsbb.png')

if __name__ == "__main__":
    main()