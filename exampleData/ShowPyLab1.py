#ShowPyLab1.py
""" Shows how to plot the values in a 1-dim numpy array.
    Uses ylabel, title, xlim, ylim, ticks, figure, and show
"""

from numpy import *
from pylab import *
from TheDaylightClass import *

City = 'Ithaca'
#  Get Rise/Set Data
C = Daylight(City)
D = C.SunUp()

# Set up an L-by-W figure  
L = 12
W = 8
figure(figsize=(L,W))
  
# Plot a 1-dim numpy array  
plot(D)

# The title
titlestr = '%s     Lat = %6.2f  Long = %6.2f' % (C.City,C.Lat,C.Long)
title(titlestr,fontsize=18,color=[0,0,0])

# Label the y-axis
ylabel('Hours of Sunlight',fontsize=16)

# set the range of x and the range of y
xlim(0,364)
ylim(5,20)
    
# Position ticks along the x-axis and label them
c = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
t = [15,45,75,105,135,165,195,225,255,285,315,345]
xticks( t,c)

# Draw a grid
for k in range(6,20):
    # Draw horizontal line from (0,k) to (65,k)
    plot(array([0,365]),array([k,k]),color='red',linestyle=':')
for k in [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]:
    # Draw vertical line from  (k,5)) to (k,20))
    plot(array([k,k]),array([5,20]),color='red',linestyle=':')
    
show()

   

        
