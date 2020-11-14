#!/usr/bin/env python3
"""
Author   : Matthew Moore
Date     : 11/13/2020
Revision : 11/13/2020
"""
from PIL import Image

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
    lhstt: Image = Image.open('test.png')
    lhstb: Image = Image.open('newTest.png')
    rhstt: Image = Image.open('rht.png')
    rhstb: Image = Image.open('rhb.png')
    lhsbt: Image = Image.open('lhsbt.png')
    lhsbb: Image = Image.open('lhsbb.png')
    rhsbt: Image = Image.open('rhsbt.png')
    rhsbb: Image = Image.open('rhsbb.png')
    
    concatenatedlt: Image = get_concat_v(lhstt, lhstb)
    concatenatedrt: Image = get_concat_v(rhstt, rhstb)
    concatenatedlb: Image = get_concat_v(lhsbt, lhsbb)
    concatenatedrb: Image = get_concat_v(rhsbt, rhsbb)
    concatenatedt: Image = get_concat_h(concatenatedlt, concatenatedrt)
    concatenatedb: Image = get_concat_h(concatenatedlb, concatenatedrb)
    
    get_concat_v(concatenatedt, concatenatedb).save('concatenated.png')

if __name__ == "__main__":
    main()