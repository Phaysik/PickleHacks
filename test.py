from LineDraw import linedraw
import random
from ProcessImages import combine
from Py2SVG import svg2gcode

def MakeThatShitIntoLines():
    namesFile = open('./Scraping/filenames.txt', 'r')
    names = namesFile.readlines()
    imageCount = len(names)
    imageIndices = []
    while(len(imageIndices) < 8):
        index = random.randint(0, imageCount-1)
        if(not imageIndices.__contains__(names[index].strip('\n'))):
            imageIndices.append('./Scraping/Images/'+names[index].strip('\n'))
    
    combine.combine(imageIndices)
            
    #lines = linedraw.sketch('concatenated.png')                                 
    svg2gcode.generate_gcode("./output/out.svg")

MakeThatShitIntoLines()