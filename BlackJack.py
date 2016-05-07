# Mini-project #6 - Blackjack
#images and flashing text: http://www.codeskulptor.org/#user40_sT60k7Vhqp_24.py
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Deal to begin a game..."
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        cards_str = ""
        for card in self.cards:
            cards_str += card.get_suit()
            cards_str += card.get_rank()
            cards_str += ' '
        return cards_str

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        any_aces = False
        
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == "A":
                any_aces = True
        if any_aces == False:
                return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                          [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]],
                          CARD_BACK_SIZE)
        for item in range(len(self.cards)):
            self.cards[item].draw(canvas, [pos[0] + (item % 5) * 100, pos[1] + (item // 5) * 100])
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.card = []

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()
    
    def __str__(self):
        # return a string representing the deck
        cards_str = ""
        for card in self.cards:
            cards_str += card.get_suit()
            cards_str += card.get_rank()
            cards_str += ' '
        return cards_str



#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand

    in_play = True
    outcome = "Hit or Stand?"
    
    player_hand = Hand()
    dealer_hand = Hand()
    card_deck = Deck()
    card_deck.shuffle()
    
    if in_play:
        player_hand.add_card(card_deck.deal_card())
        player_hand.add_card(card_deck.deal_card())
        
        dealer_hand.add_card(card_deck.deal_card())
        dealer_hand.add_card(card_deck.deal_card())

def hit():
    global in_play, score, outcome, player_hand, dealer_hand
 
    # if the hand is in play, hit the player
    if in_play and player_hand.get_value() <= 21:
        player_hand.add_card(card_deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You have busted!"
            score -= 1
            in_play = False   
   
       
def stand():
    global in_play, score, outcome, player_hand, dealer_hand
   
    in_play = False
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(card_deck.deal_card())
        
    if outcome != "Hit or Stand?":
        outcome = "Deal Again?"
        return
    
    if dealer_hand.get_value() > 21:
        score += 1
        outcome = "Dealer busts! You win!"
    else:
        if dealer_hand.get_value() > player_hand.get_value():
            score -= 1
            outcome = "Dealer Wins!"
        elif dealer_hand.get_value() < player_hand.get_value():
            score +1
            outcome = "Player Wins!"
        else:
            score -= 1
            outcome = "Draw.  House Wins!"
            
            

# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", [220, 50], 50, "Black")
    canvas.draw_text("Score:", (450, 50), 26, "White")
    canvas.draw_text(str(score), (525, 50), 26, "White")
    
    canvas.draw_text("Dealer", [10,150], 30, "Black")
    dealer_hand.draw(canvas, [100, 150])
    
    canvas.draw_text("Player", [10,300], 30, "Black")
    player_hand.draw(canvas, [100, 300])
    
    canvas.draw_text(outcome, [10,100], 26, "White")
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (136,199), CARD_BACK_SIZE)
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling

player_hand = Hand()
dealer_hand = Hand()
card_deck = Deck()

frame.start()


# remember to review the gradic rubric