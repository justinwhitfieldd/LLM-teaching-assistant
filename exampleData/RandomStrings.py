# RandomStrings.py
""" Generates an alphabetized list of random strings where
all the strings have the same specified length.
No two strings in the list are the same."""

from random import randint as randi

def RandString(m):
    """ Returns a length-m string consisting of
    lower case letters.
    
    PreC: m is a positive integer.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    w = ''
    for i in range(m):
        w = w + letters[randi(0,25)]
    return w

def ListOfRandomStrings(n,m):
    """ Returns an alphabetized length-n list of random strings
    each of which is made up of m lower case letters.
    The items in the list are distinct.
    
    PreC: n and m are positive integers and n<=26**m
    """
    s = []    # The list of strings.
    k = 0     # The current length of s.
    while k<n:
        # Generate a random string and append it to s if it is not already in s.
        w = RandString(m)
        if w not in s:
            s.append(w)
            k+=1
    s.sort()
    return s

# Application Script
if __name__ == '__main__':
    n = 1000
    m = 3
    s = ListOfRandomStrings(n,m)
    #  Print the list s, 20 items per line...    
    for k in range(n):
        if k%20==19:
            print(s[k])
        else:
            print(s[k]),
        
       
    


