
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'Queen',
    'King',
    'Ace')

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}

#TO-DO
#ACE CAN BE 1 or 11

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.suit + " of " + self.rank

class Deck:
    def __init__(self):
        self.all_cards = []
    
    def __str__(self):
        return f"Deck has {len(self.all_cards)} cards stored."
    
    def deal_one(self):
        return self.all_cards.pop(-1)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def show_deck(self):
        for card in self.all_cards:
            print(card)

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
    
    def __str__(self):
        return f"Player {self.name} has {len(self.hand)} cards in hand and {self.chips} chips remaining."
    
    def check_hand(self):
        print(f"Player {self.name} has: ")
        total_value = 0
        for card in self.hand:
            total_value = total_value + card.value
            print(" ", card)
        print(f"A total value of: {total_value}")
    
    def bet(self, amount):
        if amount > self.chips:
            return f"Player {self.name}'s bet exceeds current chips! Unable to bet!"
        else:
            return (self.chips - amount)

class Dealer:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def __str__(self):
        return f"Dealer {self.name} has {len(self.hand)} cards in hand."
    
    def check_hand(self):
        print(f"Dealer has {len(self.hand[0::-1])} Hidden Card and a {self.hand[-1]} a total value of: {self.hand[-1].value}")


def play_blackjack():
    #Instantiating Deck
    new_deck = Deck()
    for suit in suits:
        for rank in ranks:
            new_deck.all_cards.append(Card(suit, rank)) 
    new_deck.shuffle()
    print(f"A deck of {len(new_deck.all_cards)} cards has been created and shuffled!")
    
    #Instantiating Player and Dealer
    player = Player("Goldship", 50)
    dealer = Dealer("Gentildonna")
    print(f"Player {player.name} has been created!")
    print(f"Dealer {dealer.name} has been created!")
    
    print("\n Game is Starting!")
    
    #-------------Game Logic-----------------
    game_on = True
    current_bet_amount = 0
    
    while game_on == True:
        for i in range(2):
            player.hand.append(new_deck.deal_one())
            dealer.hand.append(new_deck.deal_one())
        print(player)
        print(dealer)
        
        betting = False
        
        while betting == False:
            choice = input(f"Will {player.name} make a bet? (y/n)").lower()
            
            if choice in ['y']:
                bet_amount = 'wrong'
                
                while type(bet_amount) != type(int()) or player.chips<current_bet_amount:
                    bet_amount =  int(input(f"{player.name} currently has {player.chips} chips. Please enter a viable amount: "))
                    
                    if type(bet_amount) != type(int()):
                        print("Sorry I do not understand. Please enter an amount of integers!")
                    
                    current_bet_amount = player.bet(bet_amount)
                    print(current_bet_amount)
                    
                    betting = True
                
                
            elif choice in ['n']:
                print("Cannot proceed with the game without a bet. Game ends!")
                game_on = False
                break
        
        if game_on == False:
            break
        
        #Print Player and Dealer Hands  
        dealer.check_hand()
        player.check_hand()
        
        choice = 'wrong'
        
        while choice not in ['hit', 'stay']:
            choice = input("What is your action? Type \n 1. stay, this is to keep hand. \n 2. hit, to draw another card: ")
            
            if choice not in ['hit', 'stay']:
                print("Sorry I can not understand! Please enter \n 1. stay \n 2. hit")
        
        print(choice)
        game_on = False
    

play_blackjack()

