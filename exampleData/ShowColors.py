# ShowColors.py
""" Displays the 13 built-in SimpleGraphics colors."""

from SimpleGraphics import *

MakeWindow(5,labels=False)
r =.8

DrawRect(-3,3,r,r,FillColor=MAGENTA,EdgeWidth=0)
DrawText(-2,2.8,'MAGENTA',FontSize=16)

DrawRect(-3,2,r,r,FillColor=BLUE,EdgeWidth=0)
DrawText(-2,1.8,'BLUE',FontSize=16)

DrawRect(-3,1,r,r,FillColor=YELLOW,EdgeWidth=0)
DrawText(-2,.8,'YELLOW',FontSize=16)

DrawRect(-3,0,r,r,FillColor=CYAN,EdgeWidth=0)
DrawText(-2,-.2,'CYAN',FontSize=16)

DrawRect(-3,-1,r,r,FillColor=PURPLE,EdgeWidth=0)
DrawText(-2,-1.2,'PURPLE',FontSize=16)

DrawRect(-3,-2,r,r,FillColor=RED,EdgeWidth=0)
DrawText(-2,-2.2,'RED',FontSize=16)

DrawRect(1.5,3,r,r,FillColor=PINK,EdgeWidth=0)
DrawText(2.5,2.8,'PINK',FontSize=16)

DrawRect(1.5,2,r,r,FillColor=ORANGE,EdgeWidth=0)
DrawText(2.5,1.8,'ORANGE',FontSize=16)

DrawRect(1.5,1,r,r,FillColor=GREEN,EdgeWidth=0)
DrawText(2.5,.8,'GREEN',FontSize=16)

DrawRect(1.5,0,r,r,FillColor=BLACK,EdgeWidth=0)
DrawText(2.5,-.2,'BLACK',FontSize=16)

DrawRect(1.5,-1,r,r,FillColor=DARKGRAY,EdgeWidth=0)
DrawText(2.5,-1.2,'DARKGRAY',FontSize=16)

DrawRect(1.5,-2,r,r,FillColor=LIGHTGRAY,EdgeWidth=0)
DrawText(2.5,-2.2,'LIGHTGRAY',FontSize=16)

DrawRect(-.5,-3,r,r,FillColor=WHITE,EdgeWidth=1)
DrawText(.5,-3.2,'WHITE',FontSize=16)

Title('The Built-In Colors',FontSize=24)
ShowWindow()

