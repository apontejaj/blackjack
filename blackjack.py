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
        self.busted = False
        self.blackjack = False

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
        self.busted = False
        self.blackjack = False

bet = 0
deck = []
def creating_deck():
    global deck
    deck = []
    suits = ["HEARTS", "CLUBS", "SPADES", "DIAMONS"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
         "Queen", "King"]
    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit, rank))

asking_user = lambda question: input(question)

player = None
dealer = None

def playing():
    keep_playing = True
    if counting(player) == 21:
        print ("BLACKJACK")
        keep_playing = False
        player.blackjack = True
    while keep_playing:
        valid_answer = False
        if counting(player) > 21:
            player.busted = True
            keep_playing = False
        
        while not valid_answer and not player.busted:
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
    got_card = False
    while not got_card:
        card = random.randint(0,51)
        if deck[card].available:
            turn.hand.append(card)
            deck[card].available = False
            got_card = True
            
def display_hand(turn):
    if turn == player:
        print ("I have two cards, but you can only see this one")
        print (deck[dealer.hand[0]])
        print("Your hand is:")
        for card in player.hand:
            print (deck[card])
        print ("Your score is {}".format(counting(player)))
    if turn == dealer:
        print ("This is my hand")
        for card in dealer.hand:
            print (deck[card])
        print ("My score is {}".format(counting(dealer)))
        
def counting(turn):
    score = 0
    for card in turn.hand:
        score += value(card)
    if score > 21:
        for card in turn.hand:
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

def dealer_turn():
    staying = False
    if counting(dealer) == 21:
        display_hand(dealer)
        print ("I have a BLACKJACK!")
        staying = True
        dealer.blackjack = True
    while not staying and not player.busted:
        display_hand(dealer)
        if (counting(dealer) > 16 and counting(dealer) < 21):
            print ("I decide to stay")
            staying = True
        elif counting(dealer) < 17:
            print ("I decide to hit")
            hitting(dealer)
        elif counting(dealer) > 21:
            print ("I busted")
            staying = True
            dealer.busted = True
        elif counting(dealer) == 21:
            print ("I have a 21!")
            staying = True

def winning():
    global bet
    if dealer.busted and not player.busted:
        print ("I busted, you win")
        player.balance += (2 * bet)
    elif player.busted and not dealer.busted:
        print ("You busted, that's an automatic loss, I win")
    elif dealer.blackjack and player.blackjack:
        print ("We're even")
        player.balance += bet
    elif player.blackjack and not dealer.blackjack:
        print ("Solid blackjack! You win")
        player.balance += (2.5 * bet)
    elif dealer.blackjack and not player.blackjack:
        print ("Sorry, dude. Blackjack never loses, you do!")
    elif counting(dealer) > counting (player):
        print ("I win, cause I'm closer to 21")
    elif counting(player) > counting(dealer):
        print ("You win, cause you're closer to 21")
        player.balance += (2 * bet)
    elif counting(player) == counting(dealer):
        print ("We're even")
        player.balance += bet
    bet = 0
    
def betting():
    global bet
    valid_bet = False
    print ("Your current balance is {}".format(player.balance))
    while not valid_bet:
        try:
            bet = int(asking_user("How much do you want to bet?"))
        except:
            print("That is not a valid bet")
        else:
            valid_bet = True
    player.balance = player.balance - bet
    

def begining():
    global player
    global dealer
    player = Player(asking_user("Type in your name"),1000)
    print ("Welcome {}, let's start playing".format(player.name))
    dealer = Dealer()
    another_game = True
    
    while another_game:
        player.hand = []
        player.busted = False
        player.blackjack = False
        dealer.hand = []
        dealer.busted = False
        dealer.blackjack = False

        betting()      
        creating_deck()

        hitting(player)
        hitting(dealer)
        hitting(player)
        hitting(dealer)
        display_hand(player)

        playing()

        dealer_turn()
        winning()

        valid_answer = False
        while not valid_answer:
            answer = asking_user("Do you want to play again?").lower()
            if answer == "y":
                print("Lets play again")
                valid_answer = True
            elif answer == "n":
                print("This is over")
                print("You're closing your game with {}".format(player.balance))
                valid_answer = True
                another_game = False
            else:
                print("I need a valid answer, either Y or N")

begining()

