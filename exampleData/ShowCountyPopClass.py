# ShowCountyPopClass.py
""" Sample computations with the US Census dataset downloaded from
  
  http://www.census.gov/popest/data/counties/totals/2014/CO-EST2014-alldata.html
  
The dataset is slightly modified and is in the file CensusData.csv

If c is a line in that file and v = c.split(',') then here are some
definitions:

   v[5]   State Name
   v[6]   County Name
   v[7]   2010 county population
   v[10]  2011 county population
   v[11]  2012 county population
   v[12]  2013 county population
   v[13]  2014 county population
"""
 
from GetData import fileToStringList
from TheCountyPopClass import *

# Get functions that can be used whenever it is
# necessary to sort a list of county objects based
# on population estimates from a particular year.

def getPop2010(C):
    return C.Pop2010
def getPop2011(C):
    return C.Pop2011
def getPop2012(C):
    return C.Pop2012
def getPop2013(C):
    return C.Pop2013
def getPop2014(C):
    return C.Pop2014

if __name__ == '__main__':
    """ Illustrates how to set up and sort a list of CountyPop objects."""
    TheCounties = fileToStringList('CensusData.csv')
    L = []
    for c in TheCounties:
        v = c.split(',')
        # Extract thse data of interest...
        C = CountyPop(v[6],v[5],int(v[7]),int(v[10]),int(v[11]),int(v[12]),int(v[13]))
        L.append(C)
    
    # Display the m biggest counties in 2014....
    m = 50
    print '2014:'
    L.sort(key=getPop2014,reverse=True)
    for k in range(m):
        popString = '%9d' % L[k].Pop2014
        print L[k],popString
        
        
    

    






    
        
        

 
