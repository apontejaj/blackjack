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
    def __init__(self, suit, rank, available = True, highest_value = True):
        self.suit = suit
        self.rank = rank
        self.available = available
        self.highest_value = highest_value

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
    display_hand(player)

    keep_playing = True
    if counting() == 21:
        print ("Your score is {}".format(counting()))
        print ("BLACKJACK")
        keep_playing = False

    while keep_playing:
        valid_answer = False
        busted = False
        print ("Your score is {}".format(counting()))
        if counting() > 21:
            print ("You've busted - This is an automatic loss")
            busted = True
            keep_playing = False
        
        while not valid_answer and not busted:
            answer = asking_user("Press H to hit or S to stay").lower()
            if (answer == "h" or answer == "s"):
                valid_answer = True
                if answer == "h":
                    hitting(player)
                    display_hand(player)
                elif answer == "s":
                    print ("Stay")
                    keep_playing = False
            else:
                print ("Not a valid answer")
        
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
            
def display_hand(turn):
    if turn == player:
        print ("I have two cards, but you can only see this one")
        print (deck[dealer.hand[0]])
        print("Your hand is:")
        for card in player.hand:
            print (deck[card])
    if turn == dealer:
        print ("This is my hand")
        for card in dealer.hand:
            print (deck[card])
        
def counting():
    score = 0
    for card in player.hand:
        score += value(card)
    if score > 21:
        for card in player.hand:
            if deck[card].rank == "Ace":
                if deck[card].highest_value:
                    score = score - 10
                    deck[card].highest_value = False
                    break
    return score

def value(card):
    if (deck[card].rank == "2" or deck[card].rank == "3" or
        deck[card].rank == "4" or deck[card].rank == "5" or
        deck[card].rank == "6" or deck[card].rank == "7" or
        deck[card].rank == "8" or deck[card].rank == "9" or
        deck[card].rank == "10"):
        val = int(deck[card].rank)
    elif (deck[card].rank == "Jack" or deck[card].rank == "Queen" or
          deck[card].rank == "King"):
        val = 10
    elif (deck[card].rank == "Ace"):
        if deck[card].highest_value:
            val = 11
        else:
            val = 1
    return val

playing()
