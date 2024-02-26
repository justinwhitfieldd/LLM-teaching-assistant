# ShowTitle.py
""" Shows how to set up a title."""

from SimpleGraphics import *

r = input('Enter the red value   (0<=r<=1): ')
g = input('Enter the green value (0<=g<=1): ')
b = input('Enter the blue value  (0<=b<=1): ')


MakeWindow(4,bgcolor=[r,g,b],labels=False)
s = 'red = %4.2f   green = %4.2f   blue = %4.2f' %(r,g,b)
Title(s,FontSize = 20)
ShowWindow()

