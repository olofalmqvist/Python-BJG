# Black Jack Game using OOP

from random import shuffle
import time
import sys
import os

#Clubs, Spades, Hearts, Diamonds
suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

# The card rankings
ranking = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jacket', 'Queen', 'King']

# Dict with the rankings and corresponding points
card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jacket': 10, 'Queen': 10, 'King': 10}

account = 1000
hand_points = 0
dealer_points = 0

class Card:
    def __init__(self, suit, ranking):
        self.suit = suit
        self.rank = ranking
        
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

class Hand():
    def __init__(self):
        self.cards = []
        
    def card_add(self,card):
        self.cards.append(card)
        
    def showhand(self):
        for i in self.cards:
            print(i)
        
        
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))
                
    def showdeck(self):
        for i in self.deck:
            print(i)
            
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
    
# Function to clear the console    
def cls():
    os.system('cls')
    
def intro():
    print("Welcome to the Black Jack game! \n")
    global player_name
    
    print("What is your name?\n")
    player_name = input("My name is: ")
    print("\nGood to have you playing", player_name,". What would you like to do?")
    
    while(True):
        play_or_quit = input("Type 'Play' to run the game or 'Quit' to exit the program: ").lower()
        
        if play_or_quit[0] == 'q':
                print("\nThanks for playing!")
                time.sleep(1)
                break
                exit()
            
        elif play_or_quit[0] == 'p':
            print("Okay, lets start! \n")
            for i in range(1, 4):
                time.sleep(0.5)
                print("Loading...")
            deal_cards()
            game_session()
            
        else:
            print("Please try again. Write 'Play' or 'Quit'.")
            continue

def game_session():
    global account, bet, hand_points, dealer_points
    
    print("You currently have", account, "SEK in your account.\n")
    
    print("How much would you like to bet? \n")
    while(True):
        try: 
            bet = int(input("I want to bet: "))
            if bet < 0:
                raise ValueError("You must choose a positive number.")
            elif bet > account:
                raise ValueError("You cannot bet more than your account, which is", account, "SEK.")
            account -= bet
            break
        except Exception as e:
            print("Error: ", e)
            print("You must choose a number.")
            time.sleep(2)
            cls()
            continue
    
    print("\nYou choose to bet", bet, "SEK, that means you have", account, "SEK left.\n")
    print("Dealing cards... \n")
    
    # Checking the player hand, cards and total points
    print("Your hand is: ")
    player_hand.showhand()
    
    for i in range(len(player_hand.cards)):
        temp = player_hand.cards[i].rank
        hand_points += card_values[temp]
    print ("Total points:", hand_points)
    
    # Checking the dealers hand, cards and total points
    print("The dealers hand is: ")
    dealer_hand.showhand()
    
    for i in range(len(dealer_hand.cards)):
        temp = dealer_hand.cards[i].rank
        dealer_points += card_values[temp]
    print ("Total points:", dealer_points)    
    

"""def compare_hands():
    player_hand.showhand()
    dealer_hand.showhand() """

   

intro()    