#ShowFractionClass.py
""" Illustrate a class that supports various operations on
fractions. Shows how to use overloaded "+" and "*" operators.
"""

from TheFractionClass import *

if __name__ == '__main__':
    # Set up two fractions...
    F1 = Fraction(2,7)
    print 'F1 = ',F1
    F2 = Fraction(3,11)
    print 'F2 = ',F2
    
    # Add them...
    F = F1 + F2
    print 'F1 + F2 =',F
    
    # Multiply them...
    F = F1*F2
    print 'F = F1*F2 = ',F
    
    # Negation...
    F3 = F.negate()
    print '-F = ',F3
    
    # Inversion...
    F4 = F.invert()
    print '1/F = ',F4
        
    # Computes 1 + 1/2 + 1/3 +...+ 1/n
    n = 15
    print '\nDisplay 1 + 1/2 + 1/3 + ... + 1/k  for k = 1 t0 %1d\n' % n
    s = Fraction(0)
    for k in range(1,n+1):
        s = s + Fraction(1,k)
        intString = '%3d ' % k
        print intString,s
        
        
    


