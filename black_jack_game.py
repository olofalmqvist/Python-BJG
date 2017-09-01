# Black Jack Game using OOP

from random import shuffle

#Clubs, Spades, Hearts, Diamonds
suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

# The card rankings
ranking = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

# Dict with the rankings and corresponding points
card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

class Card:
    def __init__(self, suit, ranking):
        self.suit = suit
        self.rank = ranking
        
    def showcard(self):
        print("This card is {} of {}.".format(self.rank, self.suit))

class Hand():
    def __init__(self):
        self.cards = []
        
    def card_add(self,card):
        self.cards.append(card)
        
    def showhand(self):
        for i in self.cards:
            i.showcard()
        
        
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))
                
    def showdeck(self):
        for i in self.deck:
            i.showcard()
            
    def shuffle(self):
        shuffle(self.deck)
        
    def deal(self):
        drawnCard = self.deck.pop()
        return drawnCard
                
#Start the round and deal the initial cards
def deal_cards():
    global player_hand, dealer_hand, deck
    
    # Initialize instances of deck, the player & dealer hands
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal initial cards, two for each player
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())
    

def compare_hands():
    player_hand.showhand()
    dealer_hand.showhand()

   

    