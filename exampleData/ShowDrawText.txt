# ShowText.py
""" Displays various font sizes."""

from SimpleGraphics import *

MakeWindow(4,bgcolor=WHITE,labels=False)

DrawText(-3,3,'This is 10 point font.')
DrawText(-3,2,'This is 12 point font.',FontSize=12,FontColor=MAGENTA)
DrawText(-3,1,'This is 14 point font.',FontSize=14,FontColor=BLUE)
DrawText(-3,0,'This is 16 point font.',FontSize=16,FontColor=GREEN)
DrawText(-3,-1,'This is 18 point font.',FontSize=18,FontColor=PURPLE)
DrawText(-3,-2,'This is 24 point font.',FontSize=24,FontColor=ORANGE)
DrawText(-3,-3,'This is 36 point font.',FontSize=36,FontColor=RED)

Title('DrawText Examples')
ShowWindow()

