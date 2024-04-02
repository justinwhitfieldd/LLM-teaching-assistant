# ShowDrawRect.py
""" Display various DrawStar examples. """

from SimpleGraphics import *

MakeWindow(6.5,bgcolor=BLUE,labels=False)

L=2
W=3

# Display various eWidth examples

DrawRect(-4,2,L,W,FillColor=YELLOW,EdgeColor=RED)
DrawText(-5.5,4.5,'EdgeWidth = 1',FontSize=14,FontColor=WHITE)

DrawRect(0,2,L,W,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=0)
DrawText(-1.4,4.5,'EdgeWidth = 0',FontSize=14,FontColor=WHITE)

DrawRect(4,2,L,W,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=5)
DrawText(2.5,4.5,'EdgeWidth = 5',FontSize=14,FontColor=WHITE)

# Display various theta examples

DrawRect(-4,-4,L,W,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=2)
DrawText(-5.5,-1.5,'theta = 0',FontSize=14,FontColor=WHITE)

DrawRect(0,-4,L,W,theta=30,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=2)
DrawText(-1.4,-1.5,'theta = 30',FontSize=14,FontColor=WHITE)

DrawRect(4,-4,L,W,theta=-30,FillColor=YELLOW,EdgeColor=RED,EdgeWidth=2)
DrawText(2.5,-1.5,'theta = -30',FontSize=14,FontColor=WHITE)

Title('DrawRect Examples')
ShowWindow()