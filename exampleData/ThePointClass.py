# ThePointClass.py

from math import sqrt, sin, cos, pi
from random import uniform as randu

class Point:
    """
    Attributes:
        x: float, the x-coordinate of a point
        y: float, the y-coordinate of a point
    """
    def __init__(self,x,y):
        """ Creates a point.
        PreC: x and y are floats
        """
        self.x = x
        self.y = y

    def __str__(self):
        """ Pretty prints a point object.
        
        To apply this function to a point P, write
              print P
        """
        return '(%6.3f,%6.3f)' %(self.x,self.y)
    

    def Dist(self,other):
        """ Returns a float that is the distance from self to other.
    
        PreC: self and other are points
        """
        d = sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return d


    def Rotate(self,theta):
        """ Returns a point that is obtained by rotating self about the
        origin theta degrees in the counterclockwise direction.
        
        PreC: self is a point and theta is a number.
        """
        x = self.x
        y = self.y
        c = cos(pi*(theta/180.0))
        s = sin(pi*(theta/180.0))
        return Point(x*c-y*s,x*s+y*c)


    def Reflect(self):
        """ Returns a point that is obtained by reflecting self about the
        the 45-degree line y = x
        
        PreC: self is a point.
        """
        x = self.x
        y = self.y
        P = Point(y,x)
        return P


    





    


    
    

