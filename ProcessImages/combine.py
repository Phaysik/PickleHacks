#!/usr/bin/env python3
"""
Author   : Matthew Moore
Date     : 11/13/2020
Revision : 11/13/2020
"""
from PIL import Image
from typing import List
import sys

def get_concat_h(im1: Image, im2: Image) -> Image:
    dst: Image = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1: Image, im2: Image) -> Image:
    dst: Image = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def main() -> None:
    if len(sys.argv) != 9:
        print('You must pass at least 8 arguments to this python file')
        quit(0)
        
    images: List[Image] = []
    for i in range(8):
            images.append(Image.open(f'{sys.argv[i + 1]}'))
    
    concatenatedlt: Image = get_concat_v(images[0], images[1])
    concatenatedrt: Image = get_concat_v(images[2], images[3])
    concatenatedlb: Image = get_concat_v(images[4], images[5])
    concatenatedrb: Image = get_concat_v(images[6], images[7])
    concatenatedt: Image = get_concat_h(concatenatedlt, concatenatedrt)
    concatenatedb: Image = get_concat_h(concatenatedlb, concatenatedrb)
    
    get_concat_v(concatenatedt, concatenatedb).save('concatenated.png')

if __name__ == "__main__":
    main()