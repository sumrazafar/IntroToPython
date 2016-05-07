# "Guess the number" mini-project

# Libraries required
import simplegui
import random
import math

# initialize global variables 
num_range = 100
secret_number = 0
guesses_left = 0

# helper function to start and restart the game
def new_game():
    # state global variables to be used in function
    global num_range
    global secret_number
    global guesses_left
    
    #randomly guess the number within th range
    secret_number = random.randrange(0, num_range)
    
    #assign guesses allowed
    if num_range == 100 : 	
        guesses_left = 7
    elif num_range == 1000 :
        guesses_left = 10
      
    print "... New game. The range is from 0 to", num_range, ". Good luck!"
    print "Total number of guesses available are: ", guesses_left, "\n"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a game 
    global num_range
    num_range = 100 # button that changes range to range [0,100) and restarts
    new_game() 

def range1000():
    # button that changes range to range [0,1000) and starts a game
    global num_range
    num_range = 1000 
    new_game()
    
def input_guess(guess):
    # main game logic 
    global guesses_left
    global secret_number 
    
    won = False
    
    print "You guessed: ",guess
    
    if int(guess) == secret_number:       
        won = True
    elif int(guess) > secret_number:
        result = "Go Lower!"
    else:
        result = "Go Higher!"  
        
    if won != True:    
        guesses_left = guesses_left - 1
        print "Number of remaining guesses is ", guesses_left
       
    if won:
        print "That is correct! Congratulations!\n"
        new_game()
        return
    elif guesses_left == 0:
        print "Game over. You didn't guess the number in time!"  
        print "The secret number was: ", secret_number
        print""
        new_game()
        return
    else:
        print result

    
# create frame
f = simplegui.create_frame("Guess", 250, 250)
f.set_canvas_background('Orange')

# register event handlers for control elements and start frame
f.add_label("Game: Guess the number!")
f.add_button("Range is [0, 100]", range100, 100)
f.add_button("Range is [0, 1000]", range1000, 100)	
f.add_input("Enter your guess", input_guess, 100)


# call new_game 
new_game()
f.start()

