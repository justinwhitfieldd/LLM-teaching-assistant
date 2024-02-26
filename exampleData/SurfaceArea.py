# SurfaceArea.py
""" Surface Area Increase

Computes (in three different ways) the increase
in surface area of a sphere when its radius is
increased a small amount."""

from math import sqrt, pi
# Acquire the data..
r = input('Enter the radius (kilometers): ')
inc = input('Enter the radius increase (millimeters): ')
# Make sure that r and inc are floats. (Why?)
r = float(r)
inc = float(inc)
# Radius increase in kilometers...
dr = inc/10**6;
print '\nCompute/Approximate the surface area increase three ways'
print '\nSphere radius   = %10.4f kilometers' % r
print 'Radius increase = %10.4f millimeters' % inc
print '\nSurface area increase in square kilometers:'
# Compute area increase in three ways and display the results.
# Do not worry about where the formulas come from. Focus on
# how the output was nicely displayed.
del_A1 = 4*pi*((r+dr)**2 - r**2)
print '\n   Method 1: %15.12f' %del_A1
del_A2 = 4*pi*(2*r +dr)*dr
print '   Method 2: %15.12f' %del_A2
del_A3 = 8*pi*r*dr
print '   Method 3: %15.12f' %del_A3
# Modify the above so that output includes the value of r in miles, the
# value on inc in  inches, and the surface area increase  in square miles.
# Assume that 1 mile equals 1.609 kilometers.