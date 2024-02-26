# TheHandClass.py

from TheDeckClass import *

def compare(H1,H2):
    """ Returns 1 if H1 > H2, -1 if H1<H2 and 0 otherwise
    
    This comparison of Cards compares rank first, and then suit.
    
    PreC  H1 and H2 are Cards.
    """
    if H1.rank > H2.rank:
        return 1
    if H1.rank < H2.rank:
        return -1
    # At this point, we know the two cards have the same rank.
    # So compare their suits.
    if H1.suit > H2.suit:
        return 1
    if H1.suit < H2.suit:
        return -1
    # If we get this far, H1 and H2 represent the same card.
    return 0
 

class Hand(Deck):
    """ Represents a hand of playing cards. 
    
    Attributes:
        DeckOfCards: list of Card objects
                  n: int
              label: str 
        
        n is the number of cards in the deck.
        
        The "top" of the deck is self.DeckOfCards[0]
        The "bottom" of the deck is self.DeckOfCards[self.n]
        
        label is a string that "names" the hand.
    """
    def __init__(self,label):
        """ Creates a reference to a Hand object which is initialized as a labeled empty
        hand.
        
        PreC: label is a string that names the hand
        """
        self.DeckOfCards = []
        self.n = 0
        self.label = label
        
    def __str__(self):
        """ Returns a string s such that print s
        nicely displays self.
        """
        s = self.label + ':'+'\n'
        for c in self.DeckOfCards:
            s = s + ' ' + str(c) + '\n'
        return s

    
    def sort(self):
        """ Modifies self.DeckOfCards so that it is sorted using the
        compare function MyCompare.
        """
        self.DeckOfCards.sort(compare)
    
  
    
