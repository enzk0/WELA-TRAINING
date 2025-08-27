
# CARD
# SUIT, RANK, VALUE
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

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    card_list = []
    
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                current_card = Card(suit, rank)
                self.all_cards.append(current_card)
            
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

player_one = Player("Goldship")
player_two = Player("Gentildonna")

new_deck = Deck()
new_deck.shuffle()

def deal_cards():
    while len(new_deck.all_cards) != 26:
        current_card = new_deck.deal_one()
        
        player_one.all_cards.append(current_card)

    while len(new_deck.all_cards) != 0:
        current_card = new_deck.deal_one()
        
        player_two.all_cards.append(current_card)

deal_cards()

print(player_one)
print(player_two)



game_on = True
at_war = True

round_num = 0

def check_empty():
    if len(player_one.all_cards) == 0:
        print(f"Player {player_one.name} is out of cards! Player {player_two.name} wins!")
        game_on = False
    
    if len(player_two.all_cards) == 0:
        print(f"Player {player_two.name} is out of cards! Player {player_one.name} wins!")
        game_on = False
        
while game_on == True:
    round_num += 1
    print(f"Round {round_num}")
    
    check_empty()
    
    #starting a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    while at_war == True:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
            
            check_empty()
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            at_war = False
            
            check_empty()
        
        else:
            print("WAR!")

            if len(player_one.all_cards) < 3:
                print(f"{player_one.name} unable to declare war...")
                print(f"{player_two.name} wins!!!")
                
                game_on = False
                break
            
            elif len(player_two.all_cards) < 3:
                print(f"{player_two.name} unable to declare war...")
                print(f"{player_one.name} wins!!!")
                
                game_on = False
                break
            
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
            
            