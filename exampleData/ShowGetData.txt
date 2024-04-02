# ShowGetData.py
""" This module illustrates how to use the functions in
GetData.py to count the number of lines, words, and chracters in
a text file.
"""

from GetData import fileToStringList, stringToWordList

# Create a list os strings that house all the data in a text file...
NameOfFile = 'PridePrej.txt'
L = fileToStringList(NameOfFile)
# Note that len(L) is the number of lines in the file.
nLines = len(L)
# nChars = the number of characters 
nChars = 0
# nWords = the number of words
nWords = 0
for s in L:
    nChars += len(s)
    nWords += len(stringToWordList(s))

print '\nFile : %s \n' % NameOfFile     
print 'Number of lines       = %7d' % nLines
print 'Number of words       = %7d' % nWords
print 'Number of characters  = %7d' % nChars