#ShowPyLab3.py
""" Shows how to make bar plots and to put several
graphs in the same window using subplot
"""

from numpy import *
from pylab import *
from TheDaylightClass import *

City1 = 'Johannesburg'
City2 = 'Anchorage'

figure(figsize=(12,8))

# sublot (m,n,p) means "we have m rows plots with n plots per row.
# The next goes into plot window p.

subplot(2,1,1)
#  Get Ithaca Rise/Set Data
C1 = Daylight(City1)
M = C1.MonthAves()
M1 = M[1:13]
bar(range(12),M1,facecolor='magenta')
c = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
t = [.5, 1.5, 2.5 ,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5]
xticks( t,c)
xlim(-.2,12)
ylim(0,20)
ylabel('Average Hours of Sunlight',fontsize=16)
title(C1.City,fontsize=16)

subplot(2,1,2)
C2 = Daylight(City2)
M = C2.MonthAves()
M2 = M[1:13]
bar(range(12),M2,facecolor='cyan')
xticks(t,c)
xlim(-.2,12)
ylim(0,20)
ylabel('Average Hours of Sunlight',fontsize=16)
title(C2.City,fontsize=16)


show()



