# Radius.py
# Charles Van Loan
# January 1, 2015
""" Read in the area of a circle and displays its radius.
"""
from math import sqrt,pi
A = input('Enter the circle area: ')
r = sqrt(A/pi)
print 'The radius is %6.3f' % r

