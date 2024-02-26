# Show2DUniform.py
""" Illustrates the uniform distribution
in two dimensions."""

from SimpleGraphics import *
from random import uniform as randu

N = 10000
# Display the target with random dart throws using randu
MakeWindow(1,bgcolor=CYAN)
DrawDisk(0,0,1,FillColor=YELLOW,EdgeWidth=1)
count = 0;
for k in range(N):
    # Throw the kth dart and display
    x = randu(-1,1)
    y = randu(-1,1)
    if x**2+y**2<=1:
        count+=1
    DrawDisk(x,y,.01,FillColor=RED)
MyPi  = float(4*count)/float(N)
Title('N = %4d     MyPi = %6.3f'% (N,MyPi))
ShowWindow()

