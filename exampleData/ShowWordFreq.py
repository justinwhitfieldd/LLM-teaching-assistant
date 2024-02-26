# ShowWordFreq.py
""" Illustrates the idea of a word frequency
dictionary.
"""
from GetData import FileToList, stringToWordList

def Update(wList,D):
    """ Updates the dictionary D based on the values in wList.
           D[w] += wList.count(w) if w is in D.
           D[w] =  wList.count(w) if w is not in D
    
    PreC: D is a dictionary where each key is a string (in lower case)
    and each value is an int. wList is a list of strings. 
    """
    for w in wList:
        z = w.lower()
        if z in D:
            D[z]+=1
        else:
            D[z]=1

def WordFreq(L):
    """ Returns a dictionary whose keys are words and whose
    values are ints. Each value is the number of times that the
    corresponding key occurs amongst all the strings in L.
    
    PreC: L is a list of strings.
    """
    D = {}
    for s in L:
        v = stringToWordList(s)
        Update(v,D)
    return D
    
if __name__ == '__main__':
    """ A "unique big word" is a word with length >=15 and which occurs
    only once in Pride and Prejudice. This script prints all the unique
    big words in alphabetical order."""
    L = FileToList('PridePrej.txt')
    D = WordFreq(L)
    z = D.keys()
    z.sort()
    for x in z:
        if D[x]==1 and len(x)>=15:
            print x

    

    