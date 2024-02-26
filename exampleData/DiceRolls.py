# DiceRolls.py

""" Ilustrates the use of random.randint by simulating a
dice game. """

from random import randint as randi

# Repeatedly roll 3 dice and use the outcomes to estimate
# the probability that the 3 throws are each different.
# N is the number of trials and count keeps track of the number
# of trials where the 3 dice have distinct values
N = 1000000
count = 0
print '\n   Throws       Prob Estimate'
print '------------------------------'
for k in range(1,N+1):
    # The k-th trial
    d1 = randi(1,6)
    d2 = randi(1,6)
    d3 = randi(1,6)
    if d1!=d2 and d2!=d3 and d3!=d1:
        count +=1
    if k%100000==0:
       # Look at the emerging probability estimate every 100000 throws
       print '  %8d       %8.6f ' % (k,float(count)/float(k))







       
