# TheDiskClass.py
""" Contains a class that can be used for representing
disks in the plane.
"""

from ThePointClass import *

class Disk:
    """
    Attributes:
        center: Point, the center of the disk
        radius: float, the radius of the disk
        
    """
    def __init__(self,P,r):
        """ Creates a Disk object with center P and radius r
        PreC: P is a Point and r is a positive float
        """
        self.center = P
        self.radius = r

    def Intersects(self,other):
        """ Returns True if self and other intersect and False otherwise
        PreC: self and other are disks
        """
        # The center-to-center distance:
        c1 = self.center
        c2 = other.center
        d = c1.Dist(c2)
        # The sum of the two radii
        radiusSum = self.radius + other.radius
        TheyIntersect = (radiusSum >= d )
        return TheyIntersect

