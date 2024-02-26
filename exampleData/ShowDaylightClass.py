# ShowDaylightClass.py
""" This module illustrates the the methods that are
part of the class Daylight
"""

from TheDaylightClass import *
              
MyCities = (['Anchorage','London','Ithaca','NewYork','Cairo','Miami','Lagos','Johannesburg','Sydney'])
print '\nAverage Sun-Up (Hours):\n'
print '              City     Latitude     June   September  December   March'
print '--------------------------------------------------------------------------'
for C in MyCities:
    A = Daylight(C)
    L = A.Lat
    M = A.MonthAves()
    print '%20s  %8.2f    %6.2f    %6.2f    %6.2f    %6.2f  ' % (C,L,M[6],M[9],M[12],M[3])
        
  
    

    
 
    
