# ShowDrawPoly.py
""" Draw a hexagon. """

from SimpleGraphics import *

MakeWindow(1.3,bgcolor=CYAN,labels=False)

r = 1.2

# Display various eWidth examples

x = [1, .8 , -.4 , -.5 , .0  , .7]
y = [0 , .3 ,  .8 ,  -.4 ,  -1.2 ,  -.8]
DrawPoly(x,y,FillColor=YELLOW,EdgeColor=MAGENTA,EdgeWidth=5)

Title('A Hexagon Using DrawPoly')
ShowWindow()

