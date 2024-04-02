# ShowDrawLineSeg.py
""" Displays a collection of line segments with varying line widths """

from SimpleGraphics import *
MakeWindow(4,bgcolor=WHITE,labels=False)

DrawText(-3,2.9,'LineWidth = 1',FontSize=16,FontColor=BLACK)
DrawLineSeg(-.5,3,2.5,3,LineWidth=1,LineColor=MAGENTA)

DrawText(-3,1.9,'LineWidth = 2',FontSize=16,FontColor=BLACK)
DrawLineSeg(-.5,2,2.5,2,LineWidth=2,LineColor=MAGENTA)

DrawText(-3,.9,'LineWidth = 3',FontSize=16,FontColor=BLACK)
DrawLineSeg(-.5,1,2.5,1,LineWidth=3,LineColor=MAGENTA)

DrawText(-3,-.1,'LineWidth = 4',FontSize=16,FontColor=BLACK)
DrawLineSeg(-.5,0,2.5,0,LineWidth=4,LineColor=MAGENTA)

DrawText(-3,-1.1,'LineWidth = 5',FontSize=16,FontColor=BLACK)
DrawLineSeg(-.5,-1,2.5,-1,LineWidth=5,LineColor=MAGENTA)

DrawText(-3,-2.1,'LineWidth = 6',FontSize=16,FontColor=BLACK)
DrawLineSeg(-.5,-2,2.5,-2,LineWidth=6,LineColor=MAGENTA)

DrawText(-3,-3.1,'LineWidth = 7',FontSize=16,FontColor=BLACK)
DrawLineSeg(-.5,-3,2.5,-3,LineWidth=7,LineColor=MAGENTA)

Title('DrawLineSegment Examples')
ShowWindow()