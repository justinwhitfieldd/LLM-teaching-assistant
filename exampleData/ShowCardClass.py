#ShowCardClass.py
""" Illustrates the methods in the Card class.
"""
from TheCardClass import *

print '\n      Your Card              My Card         Winner '
print '------------------------------------------------------'
for k in range(7):
    # Select two random cards from a complete deck
    # and see who beats who..
    YourCard = Card()
    MyCard   = Card()
    if YourCard > MyCard:
        Winner = '     You'
    elif MyCard > YourCard:
        Winner = '     Me'
    else:
        Winner =  '     Tie'
    print YourCard, MyCard,Winner

        
