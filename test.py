from LineDraw import linedraw
import random
from ProcessImages import combine
def MakeThatShitIntoLines():
    namesFile = open('./Scraping/filenames.txt', 'r')
    names = namesFile.readlines()
    imageCount = len(names)
    imageIndices = []
    while(len(imageIndices) < ):
        index = random.randint(0, imageCount-1)
        if(not imageIndices.__contains__(names[index])):
            imageIndices.append(names[index])
    

            
    #lines = linedraw.sketch(imagePath)                                 
    #linedraw.makesvg(lines)
    #svg2gcode.generate_gcode("output/out.svg")

MakeThatShitIntoLines()