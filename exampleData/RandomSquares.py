#RandomSquares.py
""" Draws numerous random squares. The color, size, and tilt of
each squares is random. """

from random import uniform as randu
from random import randint as randi
from SimpleGraphics import *
n = 10    # Window size
N = 400   # The number of random rectangles to draw
c1 = MAGENTA
c2 = YELLOW
c3 = CYAN
MakeWindow(n,bgcolor=BLACK)
for k in range(N):
    x = randu(-n,n)
    y = randu(-n,n)
    s = randu(0,n/4.)
    i= randi(1,3)
    tau = randi(0,45)
    if i%3==0:
       DrawRect(x,y,s,s,FillColor=c1,EdgeWidth=3,theta=tau)
    elif i%3==1:
       DrawRect(x,y,s,s,FillColor=c2,EdgeWidth=3,theta=tau)
    else:
       DrawRect(x,y,s,s,FillColor=c3,EdgeWidth=3,theta=tau)
ShowWindow()
