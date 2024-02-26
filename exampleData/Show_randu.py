# Show_randu.py
"""Shows how to generate random floats
using random.uniform """

from random import uniform as randu

# Simulate the flipping of a coin N times

N = 1000000
a = 0
b = 1000
L = 100
R = 500
count = 0
for k in range(N):
    x = randu(a,b)
    # Convention: 1
    if L<=x<=R:
        count+=1
        
prob = float(count)/float(N)
fraction = float(R-L)/float(b-a)
print '%8.6f   %8.6f ' % (prob,fraction)