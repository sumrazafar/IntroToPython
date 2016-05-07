# Implementation of classic arcade game Pong

import simplegui
import random

# globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
TEXT_SIZE = 100
TEXT_FACE = "serif"
VELOCITY = 10

score1 = 0
score2 = 0
ball_vel = [0, 0]	#ball velocity vector
ball_pos = [0, 0]	#ball position vector 
paddle1_vel = 0		#paddle velocity
paddle2_vel = 0
paddle1_pos = 0		#paddle position
paddle2_pos = 0
right = True		#ball direction 
game_ended = True	#current ball moving status
btnSize = 150		#button size

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
# direction = TRUE for right side spawn
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global game_ended
    
    game_ended = False
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #random ball velocity
    if direction: 
        ball_vel = [random.randrange(120,240)/60, random.randrange(60,180)/60*random.choice([1, -1])]
    else:
        ball_vel = [(random.randrange(120,240) * -1)/60, random.randrange(60,180)/60*random.choice([1, -1])]
    

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    #reset all variables
    game_ended = False
    score1 = 0; score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    # when restart, random direction
    right = random.choice([True, False]) 
    spawn_ball(right)

def end_game():
    global right, score1, score2
    game_ended = True
    if right: 
        score1 += 1     
    else: 
        score2 += 1
    spawn_ball(right)
        
def update_pos(pos, vel):
    if (pos + vel <= HEIGHT - HALF_PAD_HEIGHT) and (pos + vel >= HALF_PAD_HEIGHT):
        return (pos + vel)
    else:
        return pos
        
        
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global right, game_ended
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
               
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS - 1, 1, "Orange", "Orange")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = update_pos(paddle1_pos, paddle1_vel)
    paddle2_pos = update_pos(paddle2_pos, paddle2_vel)
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],
                [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "Red")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],
                [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "Blue")
    
    # determine whether paddle and ball collide    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = ball_vel[1] * -1
        
    if ball_vel[0] < 0 and ball_pos[0] <= BALL_RADIUS: # ball heading left
        if ball_pos[1] > (paddle1_pos - HALF_PAD_HEIGHT) and ball_pos[1] < (paddle1_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = ball_vel[0] * -1
        else: # right player won
            right = True # next time ball will head right first
            if game_ended == False: end_game()
            
    if ball_vel[0] > 0 and ball_pos[0] >= (WIDTH - BALL_RADIUS): # ball heading right
        if ball_pos[1] > (paddle2_pos - HALF_PAD_HEIGHT) and ball_pos[1] < (paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = ball_vel[0] * -1
        else: # left player won
            right = False # next time ball will head left first
            if game_ended == False: end_game()
                
    # draw scores
    score_text = str(score1) + " " + str(score2)
    textwidth = frame.get_canvas_textwidth(score_text, TEXT_SIZE, TEXT_FACE)
    canvas.draw_text(score_text, ((WIDTH-textwidth)/2, 80), TEXT_SIZE, "White", TEXT_FACE)

    
# velocity updated only for specific keys used
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += VELOCITY
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= VELOCITY        
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += VELOCITY
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= VELOCITY

# reset velocity         
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0

#close frame
def quit_game():
    frame.stop()

# create frame
frame = simplegui.create_frame("** Pong **", WIDTH, HEIGHT)
frame.add_label("")
frame.add_label("Red paddle control:")
frame.add_label("w - up")
frame.add_label("s - down")
frame.add_label("")
frame.add_label("Blue paddle control:")
frame.add_label("up - up")
frame.add_label("down - down")
frame.add_label("")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# add button handlers
frame.add_button("Reset Game", new_game, btnSize)
frame.add_label("")
frame.add_button("Quit Game", quit_game, btnSize)

# start frame
new_game()
frame.start()
