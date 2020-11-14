#!/usr/bin/env python3
"""
Author   : Matthew Moore
Date     : 11/14/2020
Revision : 11/14/2020
"""

from typing import List
import sys

def main() -> None:
    if len(sys.argv) != 2:
        print('You must pass in the filename of the gcode output to this python script')
        quit(0)
    
    lines: List[str] = []
    with open(f'./gcode_output/{sys.argv[1]}.gcode', 'r') as f:
        lines = f.readlines()
        
    for i in range(len(lines)):
        if 'X' in lines[i] and 'G0' in lines[i]:
            newX: float = float(lines[i].split('X')[1].split(' ')[0]) + 40.0
            newY: float =  float(lines[i].split('Y')[1]) - 120.0
            lines[i] = f'G0 X{newX:.1f} Y{newY:.1f} F2400\n'

    with open(f'./gcode_output/{sys.argv[1]}.gcode', 'w') as f:
        for line in lines:
            f.write(f'{line}')
    
if __name__ == "__main__":
    main()
