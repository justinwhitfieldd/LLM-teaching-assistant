# ShowWords.py
""" Illustrates the function GetWords and
sets up a list of strings, each of which is an English
word.
"""

from GetData import fileToStringList

def Palindrome(s):
    """ Returns True if s is a palindrome.
    PreC: s is a string"""
    
    n = len(s)
    for k in range(n/2):
        if s[k]!=s[n-1-k]:
            return False
    return True

def Nouns(L):
    """ Returns a list of nouns.
    
    PreC: L is a list of strings, each string being an English word.
    if L[k+1] is the plural of L[k], then L[k] is a noun."""
    pass

def FirstLast(s):
    """ Returns a list of Bozos where a Bozo is a string whose
    first an last characters are the same and not consonants.
    
    PreC: """
    pass

def HaveDouble(s):
    """ Returns True if and only if s contains a length-2 substring that
    contains two of the same consonants.
    """
    pass



if __name__ == '__main__':
    # Print all palindromes that have 5 or more letters
    L = fileToStringList('EnglishWords.txt')
    for s in L:
        if len(s)>=5 and Palindrome(s):
           print s

