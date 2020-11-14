from LineDraw import linedraw

def MakeThatShitIntoLines(imagePath)
    lines = linedraw.sketch("LineDraw/peppers.png")                                 
    linedraw.makesvg(lines)