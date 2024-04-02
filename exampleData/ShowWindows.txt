# ShowWindows.py
""" Illustrates ShowWindow."""

from SimpleGraphics import *

from time import sleep as pause

# Display a sequence of three windows, each for one second.
# Then close all the windows

MakeWindow(4,bgcolor=BLACK,labels=False)
DrawText(-1.7,0,'Window 1',FontColor=YELLOW,FontSize=36)
ShowWindow(2)

MakeWindow(4,bgcolor=BLACK,labels=False)
DrawText(-1.7,0,'Window 2',FontColor=YELLOW,FontSize=36)
ShowWindow(2)

MakeWindow(4,bgcolor=BLACK,labels=False)
DrawText(-1.7,0,'Window 3',FontColor=YELLOW,FontSize=36)
ShowWindow(2)

CloseWindow()     # Remove this line to keep all three windows open

"""
# Display all three windows with no pauses.

MakeWindow(4,bgcolor=BLACK,labels=False)
DrawText(-1.7,0,'Window 1',FontColor=YELLOW,FontSize=36)

MakeWindow(4,bgcolor=BLACK,labels=False)
DrawText(-1.7,0,'Window 2',FontColor=YELLOW,FontSize=36)

MakeWindow(4,bgcolor=BLACK,labels=False)
DrawText(-1.7,0,'Window 3',FontColor=YELLOW,FontSize=36)

ShowWindow()

"""


















