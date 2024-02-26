# SimpleMath.py
""" Module to illustrate three simple math-type functions.

Very crude implementations for the square root, 
cosine, and sine functions."""

def sqrt(x):
    """Returns an approximate square root of x.
    
    Performs five steps of rectangle averaging.
    
    Precondition: The value of x is a positive number."""
    x = float(x)
    L = x 
    L = (L + x/L)/2
    L = (L + x/L)/2
    L = (L + x/L)/2
    L = (L + x/L)/2
    L = (L + x/L)/2
    return L


def cos(x):
    """Returns an approximation to the cosine of x.
    
    Uses a degree-6 polynomial.
    
    Precondition: x is a number that represents a radian value."""
    
    x = float(x)
    y = 1.0 - x**2/2 + x**4/24 - x**6/720
    return y


def sin(x):
    """Returns an approximation to the sine of x.
    
    Uses a degree-7 polynomial.
    
    Precondition: x is a number that represents a radian value."""
    
    x = float(x)
    y = x - x**3/6 + x**5/120 - x**7/5040
    return y

    
 
