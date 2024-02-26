# MonteCarloPi.py

"""
This module estimates pi by simulating a dart throw game.
A large number of darts are thrown at a square with vertices
(1,-1), (1,1),(-1,1) and (-1,-1).  The darts land anywhere
in the square with equal probability. If the dart lands inside
the unit circle we call that a "hit". For a large number of throws
N, the the ratio of hits to throws should approximately equal
the ratio of the area of the circle to the area of the square.
Thus pi/4 should approximately equal hits/N.
"""

# What we need from the standard module random
from random import uniform as randu
from random import seed

N = 1000000   # Number of darts to throw
seed(0)       # For repeatability of experiments
Hits = 0
for throws in range(N):
    # Generate and check the k-th dart throw
    x = randu(-1,1)
    y = randu(-1,1)
    if x**2 + y**2 <= 1 :
        # Inside the unit circle
        Hits += 1
piEst = 4*(float(Hits)/float(N))
print '\nTotal number of dart throws = %1d' % N
print 'Pi Estimate  = %7.5f' % piEst


