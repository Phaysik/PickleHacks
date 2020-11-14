#!/usr/bin/env python3
"""
Author   : Matthew Moore
Date     : 11/13/2020
Revision : 11/13/2020
"""

from selenium import webdriver
from requests import get
from typing import List
from validators import url
import sys

def main() -> None:
    if (len(sys.argv) != 2):
        print('Only pass in one argument to the python file')
        quit(0)
        
    if (url(sys.argv[1]) != True):
        print('Only pass in a valid url to the python file')
        quit(0)
        
    driver = webdriver.Chrome()
    driver.get(sys.argv[1])
    names: List[str] = []
    
    images: List[str] = [i.get_attribute("src") for i in driver.find_elements_by_tag_name('img')]
    
    imageMax: int = 10
    
    for imageurl in images:
        if imageurl != None and ('.jpg' in imageurl or '.png' in imageurl or '.jpeg' in imageurl) and imageMax != 0:
            r = get(imageurl, stream=True, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                name: str = imageurl.split('/')[-1].split('?')[0]
                names.append(name)
                print(f'Downloading {name} to ./Images/')

                with open(f'./Images/{name}', 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
                        
                imageMax -= 1

    print('Writing the image names to a file')
    
    with open('filenames.txt', 'w') as writer:
        for name in names:
            writer.write(f'{name}\n')
    
    driver.close()
    
    print('Execution complete')

if __name__ == '__main__':
    main()