#ShowDeckClass.py
""" Illustrates the Deck class.
"""
from TheDeckClass import *
from TheCardClass import *

from copy import copy
from copy import deepcopy

# Create and Shuffle a Deck...
D = Deck()
D.shuffle()

# Select the top 5 cards, display what they are, and put back
# on the bottom of the deck
for k in range(5):
    c = D.pop_card('Top')
    print c
    D.add_card(c)
    
print
print D


    
