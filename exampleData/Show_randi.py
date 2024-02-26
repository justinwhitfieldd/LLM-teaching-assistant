# Show_randi.py
"""Shows how to generate random integers
using random.randint """

from random import randint as randi

# Simulate the flipping of a coin N times

N = 1000000
Heads = 0
Tails = 0
for k in range(N):
    i = randi(1,2)
    # Convention: 1 is "heads" and 2 is "tails"
    if i==1:
        Heads +=1
    else:
        Tails +=1
print  '    N = %7d\nHeads = %7d\nTails = %7d' %(N,Heads,Tails)