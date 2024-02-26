# TheCountyPopClass.py

from math import sqrt, sin, cos, pi
from random import uniform as randu

class CountyPop(object):
    """
    Attributes:
        Name: the name of the county     (str)
        State: the name of the state     (str)
        Pop2010:int, the 2010 population (int)
        Pop2011:int, the 2011 population (int)
        Pop2012:int, the 2012 population (int)
        Pop2013:int, the 2013 population (int)
        Pop2014:int, the 2014 population (int)
        
    """
    def __init__(self,Name,State,Pop2010,Pop2011,Pop2012,Pop2013,Pop2014):
        """ Creates a CountyPop object.
        PreC: Name and State are strings, the rest are ints.
        """
        self.Name = Name
        self.State = State
        self.Pop2010 = Pop2010
        self.Pop2011 = Pop2011
        self.Pop2012 = Pop2012
        self.Pop2013 = Pop2013
        self.Pop2014 = Pop2014
        
    def __str__(self):
        """ Pretty prints a County object.
        
        To apply this function to a point P, write
              print P
        """
        fullName = self.Name + ', ' + self.State 
        return '%40s' % fullName


    

   


    
    

