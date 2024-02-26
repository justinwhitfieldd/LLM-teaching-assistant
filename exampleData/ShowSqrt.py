# ShowSqrt.py
""" Illustrates the effect of N on the accuracy
of a sqrt function where N is the number of
rectangle averagings."""

import math
def sqrt(x,N=5):
    """ Returns a float that is an approxinmate square root
    of x. N ius the numberof rectangle averagings associated with
    the method.
    
    PreC: x is a nonnegative float and N is a positive int.
    """
    
    x = float(x)
    if x==0:
        return 0
    L = x
    for k in range(N):
        L = (L + x/L)/2
    return L
 
# Application Script   
if __name__ == '__main__':
    print '\nLook at |math.sqrt(x) - sqrt(x,N)| for various N...'
    print '\n     x        math.sqrt(x)     N=5        N=6         N=7'
    print '----------------------------------------------------------------'
    for k in range(1,11):
        x = 2**k
        yTrue = math.sqrt(x)
        y5  = sqrt(x)
        e5 = abs(y5-yTrue)
        y6 = sqrt(x,6)
        e6 = abs(y6-yTrue)
        y7 = sqrt(x,7)
        e7= abs(y7-yTrue)
        print '%10.0f  %12.6f   %10.2e  %10.2e  %10.2e' % (x,y7,e5,e6,e7)
        
