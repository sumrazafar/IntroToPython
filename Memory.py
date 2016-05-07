# implementation of card game - Memory

import simplegui
import random

WIDTH = 800
HEIGHT = 200
CARD_NUM = 16
UNIQUE_CARDS = CARD_NUM // 2
CARD_WIDTH = WIDTH // CARD_NUM

# helper function to initialize globals
def new_game():
    global cards, exposed, correct, state, previous, turns
    cards = [(i % UNIQUE_CARDS) for i in range(CARD_NUM)]
    random.shuffle(cards)
    exposed = [False for i in range(CARD_NUM)]
    correct = [False for i in range(UNIQUE_CARDS)]
    state = 0
    previous = -1
    turns = 0
    label.set_text("Turns = " + str(turns))  
    status.set_text("New Game ... Good Luck!")
    
def update(currCardIndex):
    global state, turns
    if state == 0:
        turns += 1
        state = 1
    elif state == 1:
        if previous == cards[currCardIndex]:
            correct[cards[currCardIndex]] = True            
        state = 2
    else:
        for i in range(16):
            if not correct[cards[i]]:
                exposed[i] = False
        turns += 1
        state = 1
    label.set_text("Turns = " + str(turns))
    
    if all(item == True for item in correct) == True:
        status.set_text("Game End!")
    else:
        status.set_text("Game in Progress ...")
        
    
    
# define event handlers
def mouseclick(pos):
    global exposed, previous
    for i in range(CARD_NUM):
        if pos[0] >= CARD_WIDTH * i and pos[0] < CARD_WIDTH * (i + 1) and not exposed[i]:
            update(i)
            previous = cards[i]
            exposed[i] = True
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
   for i in range(CARD_NUM):
        if exposed[i]:
            canvas.draw_text(str(cards[i]), [CARD_WIDTH * i + WIDTH / 64, HEIGHT / 2 + 20], 60, "White")
        else:
            canvas.draw_polygon([(i*CARD_WIDTH,0),((i+1)*CARD_WIDTH,0),((i+1)*CARD_WIDTH,HEIGHT),(i*CARD_WIDTH,HEIGHT),(i*CARD_WIDTH,0)],1,"Gold","Green")
    
        
        
def quit_game():
    frame.stop()
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_label("**Memory Game**")
frame.add_label("")
frame.add_button("Reset", new_game)
frame.add_button("Quit", quit_game)
frame.add_label("")
label = frame.add_label("Turns = 0")
frame.add_label("")
status = frame.add_label("New Game ... Good Luck!")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric