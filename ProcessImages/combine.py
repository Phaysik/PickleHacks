#!/usr/bin/env python3
"""
Author   : Matthew Moore
Date     : 11/13/2020
Revision : 11/14/2020
"""
from PIL import Image
from typing import List
import sys

def get_concat_h(im1: Image, im2: Image, resample: Image = Image.BICUBIC, resize_big_image: bool = False) -> Image:
    if im1.height == im2.height:
        _im1 = im1
        _im2 = im2
    elif (((im1.height > im2.height) and resize_big_image) or ((im1.height < im2.height) and not resize_big_image)):
        _im1 = im1.resize((int(im1.width * im2.height / im1.height), im2.height), resample=resample)
        _im2 = im2
    else:
        _im1 = im1
        _im2 = im2.resize((int(im2.width * im1.height / im2.height), im1.height), resample=resample)
    dst: Image = Image.new('RGB', (_im1.width + _im2.width, _im1.height))
    dst.paste(_im1, (0, 0))
    dst.paste(_im2, (_im1.width, 0))
    return dst

def get_concat_v(im1: Image, im2: Image, resample: Image = Image.BICUBIC, resize_big_image: bool = False) -> Image:
    if im1.width == im2.width:
        _im1 = im1
        _im2 = im2
    elif (((im1.width > im2.width) and resize_big_image) or ((im1.width < im2.width) and not resize_big_image)):
        _im1 = im1.resize((im2.width, int(im1.height * im2.width / im1.width)), resample=resample)
        _im2 = im2
    else:
        _im1 = im1
        _im2 = im2.resize((im1.width, int(im2.height * im1.width / im2.width)), resample=resample)
    dst: Image = Image.new('RGB', (_im1.width, _im1.height + _im2.height))
    dst.paste(_im1, (0, 0))
    dst.paste(_im2, (0, _im1.height))
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
    
    get_concat_v(concatenatedt, concatenatedb).save('./Images/concatenated.png')

if __name__ == "__main__":
    main()