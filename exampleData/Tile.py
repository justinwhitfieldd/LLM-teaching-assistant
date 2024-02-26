# Tile.py
""" Shows how to write a function that uses the
functions in simpleGraphics.
"""
from SimpleGraphics import *

def DrawTile(x,y,r,c1,c2,c3):
    """ Draws a square, a disk and a star (in that order) each with
    center (x,y). The disk and star have radius r and the sides
    of the square are tangent to the disk
    
    The rectangle has fill color c1, the disk has fill color c2, and
    the star has fill color c3.
    
    Precondition: x, y, and r are floats or ints, c1, c2, and c3 are
    rgb arrays.
    """
    DrawRect(x,y,2*r,2*r,FillColor=c1)
    DrawDisk(x,y,r,FillColor=c2)
    DrawStar(x,y,r,FillColor=c3)

#Application Script 
if __name__ == '__main__':
    """ Applies DrawTile four times.
    """
    MakeWindow(6,bgcolor=BLACK,labels=False)
    DrawTile(3,0,2,MAGENTA,PURPLE,YELLOW)
    DrawTile(-3,0,2,MAGENTA,PURPLE,YELLOW)
    ShowWindow()