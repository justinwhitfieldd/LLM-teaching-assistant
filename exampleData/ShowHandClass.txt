#ShowHandClass.py
""" Illustrates the methods in the Hand class.
"""

from TheCardClass import *
from TheDeckClass import *
from TheHandClass import *


# Create and shuffle a Deck
D = Deck()
D.shuffle()
# Set up a 5-card hand
H = Hand('CVL')
for k in range(5):
    c = D.pop_card()
    H.add_card(c)
    
print 'The original hand:\n'
print H

print 'After it is sorted by rank:\n'
H.sort()
print H

print 'After the two lowest cards have been removed:\n'
H.pop_card('Top')
H.pop_card('Top')
print H




