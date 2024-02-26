# Show2DNormal.py

""" Illustrates the normal distribution in 2 dimensions"""

from SimpleGraphics import *
from random import normalvariate as randn
from math import sqrt 

N = 5000
# Display the target with random dart throws using randn
MakeWindow(4,bgcolor=WHITE)
DrawDisk(0,0,3,FillColor=LIGHTGRAY)
DrawDisk(0,0,2,FillColor=RED)
DrawDisk(0,0,1,FillColor=YELLOW)
n1=0; n2=0; n3=0; n4=0

for k in range(N):
    x = randn(0,1)
    y = randn(0,1)
    DrawDisk(x,y,.01,FillColor=BLACK)
    d = sqrt(x**2+y**2)
    if d<=1:
        n1+=1
    elif d<=2:
        n2+=1
    elif d<=3:
        n3+=1
    else:
        n4+=1
p1 = n1/float(N); p2 = n2/float(N); p3 = n3/float(N); p4 = n4/float(N)
Title('N=%4d   probYellow=%4.2f  probRed=%4.2f  probGray=%4.2f  probWhite=%4.2f'%(N,p1,p2,p3,p4),FontSize=12) 
ShowWindow()

