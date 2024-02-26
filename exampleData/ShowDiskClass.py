# ShowDiskClass.py
""" A module for getting practice with objects
by playing with the Disk class.
"""

from SimpleGraphics import *
from random import uniform as randu
from ThePointClass import *
from TheDiskClass import *


def outsideAll(D0,L):
    """ Returns True if and only if D0 does not intersect any
    of the disks represented in L.
    
    PreC: D0 is a Disk object and L is a list of Disk objects
    """
    for D in L:
        if D.Intersects(D0):
            return False
    return True
    

def RandomDisk(n):
    """ Returns a randomly located radius-1 disk whose center
    is inside the 2n-by-2n square centered at (0,0).
    
    Pre: n is a positive int
    """
    x = randu(-n,n)
    y = randu(-n,n)
    center = Point(x,y)
    radius = 1
    return Disk(center,radius)
    
def ShowDisk(D,c):
    """ Displays D with color c
    
    PreC: D is a Disk
    """
    xc = D.center.x
    yc = D.center.y
    r = D.radius
    DrawDisk(xc,yc,r,FillColor=c)
    
 
        
if __name__ == '__main__':
    """ This script displays non-intersecting unit
    disks in a given square window.
    """
    # The window is a square centered at (0,0) and side 2b where
    n = 10
    MakeWindow(n,bgcolor=BLACK)
    # We will attempt to display m disks in the window where
    m = 100
    # The list of displayed disks
    DiskList = []
    for k in range(m):
        D = RandomDisk(n-1)
        # We will only displayD id it does not intersect any of the
        # disks that are already displayed...
        if outsideAll(D,DiskList):
            # D does not intersect any of the displayed disks
            ShowDisk(D,MAGENTA)
            DiskList.append(D)
    # Some statistics...
    nDisplayed = len(DiskList)
    r = nDisplayed/float(m)
    Title('m = %3d  nDisplayed = %3d  ratio = %5.2f' % (m,nDisplayed,r))
    ShowWindow()
    


