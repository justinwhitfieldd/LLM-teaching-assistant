# Checkers.py
""" Looks at iteration in the context of drawing patterns.
In this case, the pattern is a checkerboard."""

from SimpleGraphics import *

def DrawRow(x0,y0,s,n,c1,c2):
    """ Draws a horizontal row of s-by-s suqares. The
    center of the leftmost square is (x0,y0) and the
    first two leftmost squares have colors c1 and c2
    respectively.
    
    PreC: x0, y0, and s are floats, n is a positive integer, c1 and
    c2 are rgb arrays."""
    
    # (xc,yc) is the center of the next square to draw.
    xc = x0
    yc = y0
    for k in range(n):
        # Draw the kth square
        if k%2==0:
           # The even-index squares have color c1
           DrawRect(xc,yc,s,s,FillColor=c1,EdgeWidth=0)
        else:
           # The odd-indexed squares have color c2
           DrawRect(xc,yc,s,s,FillColor=c2,EdgeWidth=0)
        # The next square is shifted s units to the right
        xc = xc+s

if __name__ == '__main__':
   """ Draws a checkerboard."""
   
   # The checkerboard is n-by-n and the squares are s-by-s
   n = 8
   s = 1
   # The lower left square has center at (x0,y0)
   x0 = -s*(n-1)/2.0
   y0 = -s*(n-1)/2.0
   # The checkerboard colors are c1 and c2
   c1 = RED
   c2 = WHITE
   MakeWindow((n+2)*s/2,bgcolor=BLACK,labels=True)
   # y is the vertical coordinate of the next row to draw
   y = y0
   for k in range(n):
       # Draw the kth row
       if k%2==0:
            DrawRow(x0,y,s,n,c1,c2)
       else:
            DrawRow(x0,y,s,n,c2,c1)
       # The next row is up s units
       y = y+s
        
   ShowWindow()
