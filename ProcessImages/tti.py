#!/usr/bin/env python3
"""
Author   : Matthew Moore
Date     : 11/13/2020 
Revision : 11/13/2020
"""

from PIL import Image, ImageDraw
import sys
from typing import List
from random import randint

def main() -> None:
    caption: List[str] = []
    with open("./Phrase.txt", 'r') as f:
        lines: List[str] = [i.replace('\n', '') for i in f.readlines()]
        for i in range(4):
            choice: int = randint(0, len(lines)-1)
            caption.append(lines[choice])
            lines.remove(lines[choice])
            caption.append(f"file{i}")
        
    for i in range(0, 8, 2):
        img: Image = Image.new('RGB', (756, 100), "white")

        d: ImageDraw = ImageDraw.Draw(img)

        d.text((60, 60), caption[i], fill=(0, 0, 0))

        print(f"Saving {caption[i + 1]}.png to Images/")
        img.save(f'./Images/{caption[i + 1]}.png')
    

if __name__ == "__main__":
    main()