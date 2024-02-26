# ShowDrawDisk.py
""" Display various DrawDisk examples. """

from SimpleGraphics import *

MakeWindow(6.5,bgcolor=BLUE,labels=False)
r = 1.6


# Display various eWidth examples

DrawDisk(-4,2,r,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=0)
DrawText(-5.5,4.5,'EdgeWidth = 0', FontSize=14,FontColor=WHITE)

DrawDisk(0,2,r,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=1)
DrawText(-1.4,4.5,'EdgeWidth = 1',FontSize=14,FontColor=WHITE)

DrawDisk(4,2,r,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=4)
DrawText(2.5,4.5,'EdgeWidth = 4',FontSize=14,FontColor=WHITE)

DrawDisk(-4,-4,r,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=8)
DrawText(-5.5,-1.5,'EdgeWidth = 8',FontSize=14,FontColor=WHITE)

DrawDisk(0,-4,r,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=12)
DrawText(-1.4,-1.5,'EdgeWidth = 12',FontSize=14,FontColor=WHITE)

DrawDisk(4,-4,r,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=16)
DrawText(2.5,-1.5,'EdgeWidth = 16',FontSize=14,FontColor=WHITE)

Title('DrawDisk Examples')
ShowWindow()

