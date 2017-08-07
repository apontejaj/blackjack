import random

class Player(object):
    '''
    The player class describes the player.

    Attributes:
    neme: A string indictating the name of the player
    balance: An integer indicating the money tha player has available
    '''
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []

    def __str__(self):
        return "[ {}, your balance is {} ]".format(self.name, self.balance)

class Card(object):
    def __init__(self, suit, rank, available = True):
        self.suit = suit
        self.rank = rank
        self.available = available

    def __str__(self):
        return "[ {} / {} ]".format(self.suit, self.rank)

class Dealer(object):
    def __init__(self):
        self.hand = []

deck = []
def creating_deck():
    suits = ["HEARTS", "CLUBS", "SPADES", "DIAMONS"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
         "Queen", "King"]
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit, rank))
creating_deck()

asking_user = lambda question: raw_input(question)

player = None
dealer = None
def playing():
    global player
    global dealer
    player = Player(asking_user("Type in your name"),1000)
    dealer = Dealer()
    print ("Welcome {}, let's start playing".format(player.name))
    hitting(player)
    hitting(player)
    hitting(dealer)
    hitting(dealer)

def hitting(turn):
    global player
    global dealer
    got_card = False
    while not got_card:
        card = random.randint(0,51)
        if deck[card].available:
            if turn == player:
                player.hand.append(card)
            if turn == dealer:
                dealer.hand.append(card)
            deck[card].available = False
            got_card = True            
            
playing()
print (player.hand)
print (dealer.hand)

