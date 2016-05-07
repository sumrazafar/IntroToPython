# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

#required library
import random

# helper functions

def name_to_number(name):
    #returns a number to the name
    result = -1
    
    if (name == "rock"):
        result = 0
    elif (name == "Spock"):
        result = 1
    elif (name == "paper"):
        result = 2
    elif (name == "lizard"):
        result = 3
    elif (name == "scissors"):
        result = 4
    else:
        print "Error in function 'name_to_number': Invalid name given"
        
    return result


def number_to_name(number):
    #returns a name for the number
    result = ""
    
    if (number == 0):
        result = "rock"
    elif (number == 1):
        result = "Spock"
    elif (number == 2):
        result = "paper"
    elif (number == 3):
        result = "lizard"
    elif (number == 4):
        result = "scissors"
    else:
        print "Error in function 'number_to_name': Invalid name given"
        
    return result

def rpsls(player_choice): 
    # commutes the result of the game
    
    print("")

    print "Player chooses " + player_choice

    player_number = name_to_number(player_choice)
    
     #handle the error
    if(player_number == -1):
        print "Player input inconclusive"
        return
    
    comp_number = random.randrange(0, 5)
    
    comp_choice = number_to_name(comp_number)
    
    #handle the error
    if(comp_choice == ""):
        print "Computer input inconclusive"
        return
    
    print "Computer chooses " + comp_choice

    result = (comp_number - player_number) % 5
    
    if(result == 0):
        print "Player and computer tie!"
    elif(result <= 2):
        print "Computer wins!"
    else:
        print "Player wins!"
    

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


