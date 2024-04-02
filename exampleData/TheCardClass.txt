# TheCardClass.py
""" Contains the Card class."""

from random import randint as randi

class Card(object):
    """ Represents a playing card.
    
    Attributes:
        suit: an int that encodes the suit,
              0=Clubs, 1=Diamonds, 2=Hearts, 3=Spades
        rank: an int that encodes the rank,
              1='Ace',2='Two',...,10='Ten',11='Jack',12='Queen',13='King'
    """
    
    # Class variables
    suit_names = ['Clubs','Diamonds','Hearts','Spades']
    rank_names = [None,'Ace','Two','Three','Four','Five','Six',
                 'Seven','Eight','Nine','Ten','Jack','Queen','King']
    
    def __init__(self,suit=None,rank=None):
        """Returns a  card object that represents a
        card whose suit is specified by suit and whose rank is
        specified by rank.
        
        Calls of the form Card() return a random card.
        
        Pre: suit is an int that satisfies 0<=suit<=3
             rank is an int that satisfies 1<=rank<=13
        """
        if suit==None and rank==None:
            self.suit = randi(0,3)
            self.rank = randi(1,13)
        else:
            self.suit = suit
            self.rank = rank
        
    def __str__(self):
        """ Returns a string s such that print s
        nicely displays self.
        """
        i = self.suit   # suit index
        theSuit = self.suit_names[i]
        j = self.rank   # rank index
        theRank = self.rank_names[j]
        s =  theRank+'-of-'+theSuit 
        blanks = '                              '
        return  blanks[:8-len(theRank)]+theRank+' of '+theSuit+blanks[:8-len(theSuit)]
    
    def __cmp__(self,other):
        """ Returns 1 if self>other, -1 if self<other, and 0 if
        self and other represent the same card.
        """
        # Spades beats Hearts beats Diamonds beats Ckubs
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # If the cards are from the same suit, then
        # King beats Queen beats Jack beats ten beats ... beats two beats ace
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        # If we "get this far" then the two cards are the same
        return 0
        



   
    
    
    
                  

