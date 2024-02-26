# ShowCounties.py
""" Sample computations with the US Census dataset that was downloaded from
  
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
TheCounties = fileToStringList('CensusData.csv')

# Total population
pop = 0;
for c in TheCounties:
    v = c.split(',')
    pop+=int(v[7])
print '\nUSA Population in 2010 = %1d\n' % pop

# The county with the biggest percentage growth in population...
growthMax = 0
for c in TheCounties:
    v = c.split(',')
    growth = float(v[13])/float(v[7])
    if int(v[7])>=100000 and growth>growthMax:
        growthMax = growth
        vMax = v
print vMax[6],vMax[5],'grew by',int(growthMax*100),'percent'

  
    
        
        

 
