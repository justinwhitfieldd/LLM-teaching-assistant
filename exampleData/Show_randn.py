# Show_randn.py
""" This module affirms that random.normalvariate(mu,sigma)
generates random numbers from the normal distribution with
specified mean and standard deviation.
"""

from math import sqrt 
from random import normalvariate as randn

mu = input('Enter the mean: ')
sigma = input('Enter the standard deviation: ')
N = input('Enter the number of trials: ')
sum1 = 0
sum2 = 0
for k in range(N):
    x = randn(mu,sigma)
    sum1 += x
    sum2 += (x-mu)**2
mu_tilde = float(sum1)/float(N)          # Estimated mean
sigma_tilde = sqrt(float(sum2)/float(N)) # Estimated standard deviation
print 'Estimated Mean = %10.6f' % mu_tilde
print 'Estimated std  = %10.6f' % sigma_tilde

   

