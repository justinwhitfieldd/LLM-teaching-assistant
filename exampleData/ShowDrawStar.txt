# ShowDrawStar.py
""" Display various DrawStar examples. """

from SimpleGraphics import *

MakeWindow(6.5,bgcolor=BLUE,labels=False)

r = 1.8

# Display various eWidth examples

DrawStar(-4,2,r,FillColor=YELLOW,EdgeColor=RED)
DrawText(-5.5,4.5,'EdgeWidth = 1',FontSize=14,FontColor=WHITE)

DrawStar(0,2,r,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=0)
DrawText(-1.4,4.5,'EdgeWidth = 0',FontSize=14,FontColor=WHITE)

DrawStar(4,2,r,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=5)
DrawText(2.5,4.5,'EdgeWidth = 5',FontSize=14,FontColor=WHITE)

# Display various theta examples

DrawStar(-4,-4,r,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=2)
DrawText(-5.5,-1.5,'theta = 0',FontSize=14,FontColor=WHITE)

DrawStar(0,-4,r,theta=18,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=2)
DrawText(-1.4,-1.5,'theta = 18',FontSize=14,FontColor=WHITE)

DrawStar(4,-4,r,theta=-18,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=2)
DrawText(2.5,-1.5,'theta = -18',FontSize=14,FontColor=WHITE)

Title('DrawStar Examples')
ShowWindow()

