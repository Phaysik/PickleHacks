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
    
    path: str = sys.argv[1].split('/')[3]
    
    with open(f'./gcode_output/{path}.gcode', 'r') as f:
        lines: List[str] = f.readlines()
        hold: List[str] = []
        hold.append(lines[0])
        
        for i in range(1, len(lines) - 1):
            if 'G28' not in lines[i]:
                hold.append(lines[i])
                
        hold.append(lines[len(lines) - 1])
        
    with open(f'./gcode_output/{path}.gcode', 'w') as f:
        for line in hold:
            f.write(line)

if __name__ == "__main__":
    main()