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
        
    def showhand(self, x):
        if x == 'all':
            for i in self.cards:
                print(i)
        elif x == 'one':
            print(self.cards[0])
            
        
        
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

# Start function where the player enters his name. 
def start():
   print("Welcome to the Black Jack game! \n")
   global player_name, account
   
   account = 1000
    
   print("What is your name?\n")
   player_name = input("My name is: ")
   
   # Initialize the "menu" - Quit or Play
   intro()
 
# Menu where the player can Quit or Play
def intro():
    print("\nGood to have you playing", player_name,". What would you like to do?")
    
    # Clear points from previous round, otherwise set to zero
    global player_points, dealer_points, account, game, stand
    player_points = 0 
    dealer_points = 0
    stand = False
    
    # Prepare the deck
    deal_cards()
    
    while(True):
        play_or_quit = None
        play_or_quit = input("Type 'Play' to run the game or 'Quit' to exit the program: ").lower()
        
        if play_or_quit[0] == 'q':
            print("\nThanks for playing!")
            print(play_or_quit)
            time.sleep(1)
            account = 0
            game = 'off'
            pass
            break
            exit()
            
        elif play_or_quit[0] == 'p':
            print("\nOkay, lets start! \n")
            for i in range(1, 4):
                time.sleep(0.5)
                print("Loading...")
            game_session()
            
        else:
            print("Please try again. Write 'Play' or 'Quit'.")
            continue
    

def game_session():
    global account, bet, player_points, dealer_points, game
    game = 'on'
    
    print("\nYou currently have", account, "SEK in your account.\n")
    
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
    
    ### Checking the player hand, cards and total points
    print("¤¤¤¤¤¤¤ YOUR HAND ¤¤¤¤¤¤¤\n")
    player_hand.showhand('all')
    
    # Take the sum of card ranks and store in hand_points
    for i in range(len(player_hand.cards)):
        temp = player_hand.cards[i].rank
        player_points += card_values[temp]
    print ("-------> Total points:", player_points, "\n")
    
    ### Checking the dealers hand, cards and total points
    print("##### THE DEALERS HAND #####\n")
    dealer_hand.showhand('one')
    
    # Take the sum of card ranks and sum in dealer_points (both cards)
    dealer_points = 0
    ace_list = []
    for i in range(len(dealer_hand.cards)-1):
        temp = dealer_hand.cards[i].rank
        dealer_points += card_values[temp]
        if temp == 'A':
            ace_list.append(temp)
    
    # Add points for aces in case it is beneficial for the dealer    
    if (dealer_points + 9) <= 21 and ace_list.count('A') >= 1:
        dealer_points += 9
        if (dealer_points + 9 <= 21) and ace_list.count('A') >= 2:
            dealer_points += 9
        
    print ("-------> Total points:", dealer_points)    
    
    compare_hands()
    
    while(game == 'on'):
        print("\nDo you want to hit or stand?")
        hit_or_stand = input("I choose to: ").lower()
        
        if hit_or_stand[0] == 'h':
            player_hand.card_add(deck.deal())
            ### Checking the player hand, cards and total points
            print("Your hand is: ")
            player_hand.showhand('player')
        
            # Take the sum of card ranks and store in hand_points
            player_points = 0
            ace_list = []
            for i in range(len(player_hand.cards)):
                temp = player_hand.cards[i].rank
                player_points += card_values[temp]
                if temp == 'A':
                    ace_list.append(temp)
                
            if (player_points + 9 <= 21) and ace_list.count('A') >= 1:
                player_points + 9
                if (player_points + 9 <= 21) and ace_list.count('A') >= 2:
                    player_points + 9
            print ("Total points:", player_points)
            compare_hands()
        else:
            global stand
            stand = True
            game = 'off'
            compare_hands()

def compare_hands():
    global account, bet, game, dealer_points
    
    
    while(dealer_points < 17):
        # Add another card if pounts below 17
        dealer_hand.card_add(deck.deal())    
        # Take the sum of card ranks and sum in dealer_points (both cards)
        dealer_points = 0
        ace_list = []
        for i in range(len(dealer_hand.cards)):
            temp = dealer_hand.cards[i].rank
            dealer_points += card_values[temp]
            if temp == 'A':
                ace_list.append(temp)
        
        # Add points for aces in case it is beneficial for the dealer    
        if (dealer_points + 9) <= 21 and ace_list.count('A') >= 1:
            dealer_points += 9
            if (dealer_points + 9 <= 21) and ace_list.count('A') >= 2:
                dealer_points += 9
    
    if stand == True:
        #Print out the score and the hands
        end_message()
        
        if (dealer_points >= player_points) and (dealer_points <= 21):
            print("The dealer wins. You lose", bet, "SEK.\n")
            print("You have:", account, "left in your account.\n")
            game = 'off'
            if account == 0:
                print("You have lost all your money.")
                time.sleep(3)
                exit()
            else:
                intro()
                
        else:
            print("You win this round! You gain", bet, "SEK.\n")
            account += bet*2
            print("You have:", account, "left in your account.\n")
            game = 'off'
            time.sleep(2)
            intro()
            
    elif player_points == 21:
        #Print out the score and the hands
        end_message()
        
        if dealer_points != 21:
            print("You win this round! You gain", bet, "SEK.\n")
            account += bet*2
            game = 'off'
            print("You have:", account, "left in your account.\n")
            time.sleep(2)
            intro()
        else:
            print("The dealer wins. You lose", bet, "SEK.\n")
            game = 'off'
            print("You have:", account, "left in your account.\n")
            if account == 0:
                print("You have lost all your money.")
                time.sleep(3)
                exit()
            else:
                intro()
                
    elif player_points > 21:
        #Print out the score and the hands
        end_message()
        
        print("The dealer wins. You lose", bet, "SEK.\n")
        game = 'off'
        print("You have:", account, "left in your account.\n")
        if account == 0:
            print("You have lost all your money.")
            time.sleep(3)
            exit()
        else:
            intro()
            
    else:
        pass

def end_message():
    print("\n-----THE GAME HAS ENDED!-----")
    print("You have: ")
    player_hand.showhand('all')
    print("\nWith", player_points, "number of points.\n" )
    print("The dealer has: ")
    dealer_hand.showhand('all')
    print("With", dealer_points, "number of points.\n")
    