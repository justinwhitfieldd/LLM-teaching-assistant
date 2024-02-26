# Asteroid.py

""" Illustrates how to find the minimum
amongst a number of function evaluations."""

import math
def dist(t):
    """ Returns a float that is the distance between Earth and a rogue
    asteroid at time t (days)
    
    PreC: t is a nonnegative float."""
    
    xE = 94.5*math.cos(2*math.pi*t/365)
    yE = 91.5*math.sin(2*math.pi*t/365)
    xA = 29.9*math.cos(2*math.pi*t/1000)
    yA = 100*math.sin(2*math.pi*t/1000)
    return math.sqrt((xE-xA)**2+(yE-yA)**2)
    
# Application Script
if __name__ == '__main__':
    """Find the minimum of dist(t) where t is an
    integer that satisfies L<=t<=R."""
    
    L = input('Enter initial time (integer): ')
    R = input('Enter final time (integer): ')
    
    # At any stage of the search, d_min is the smallest value of dis(t)
    # found thus far and t_min is the time associated with that minimum.
    d_min = dist(L)
    t_min = L
    for t in range(L+1,R+1):
        d_current = dist(t)
        if d_current < d_min:
            # A new minimum has been found.
            d_min = d_current
            t_min = t
    print '\n\nTime interval = [%1d,%1d]' % (L,R)
    print 'At t = %1d, the Earth-Asteroid distance is %5.0f miles' % (t_min,(10**6)*d_min)