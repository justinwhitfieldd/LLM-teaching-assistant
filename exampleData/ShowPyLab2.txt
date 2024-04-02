#ShowPyLab2.py
""" Shows how put a couple of plots in the same window
with a legend.
"""

from numpy import *
from pylab import *
from TheDaylightClass import *

figure(figsize=(12,8))

#  Get Moscow Rise/Set Data
C_Moscow = Daylight('Moscow')
D_Moscow = C_Moscow.SunUp()
plot(D_Moscow,label='Moscow',linewidth=2)

#  Get London Rise/Set Data
C_London = Daylight('London')
D_London = C_London.SunUp()
plot(D_London,label='London',linewidth=2)

#  Get Ithaca Rise/Set Data
C_Ithaca = Daylight('Ithaca')
D_Ithaca = C_Ithaca.SunUp()
plot(D_Ithaca,label='Ithaca',linewidth=2)

#  Get Miami Rise/Set Data
C_Miami = Daylight('Miami')
D_Miami = C_Miami.SunUp()
plot(D_Miami,label='Miami',linewidth=2)

#  Get Lagos Rise/Set Data
C_Lagos = Daylight('Lagos')
D_Lagos = C_Lagos.SunUp()
plot(D_Lagos,label='Lagos',linewidth=2)

#  Get Johannesburg Rise/Set Data
C_Johannesburg = Daylight('Johannesburg')
D_Johannesburg = C_Johannesburg.SunUp()
plot(D_Johannesburg,label='Johannesburg',linewidth=2)

# Possible locations for the legend:
#   upper left     upper center    upper right
#   center left    center          center right
#   lower left     lower center    lower right 

legend(loc='upper left')
legend(loc='lower middle')

ylabel('Hours of Sunlight',fontsize=16)
xlim(0,364)
ylim(5,20)
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

