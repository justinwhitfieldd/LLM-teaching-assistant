# Zeno.py
""" Draws a sequence of disks along the x-axis.
The disks are tangent to each other and each disk has
a radius that is half as big as the one to its left."""
from SimpleGraphics import *

MakeWindow(8,bgcolor=BLACK)
rc = 4.0
xc = -4.0
yc = 0.0
for k in range(10):
   DrawDisk(xc,yc,rc,FillColor=YELLOW)
   # Determine the next xc and rc
   xc = xc+1.5*rc
   rc = rc/2
ShowWindow()

