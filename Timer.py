# library
import simplegui

# define global variables
width = 600
height = width
control_width = 250
interval = 100
btnSize = 150

ticker = 0			#the counter for timer
wins = 0			#No of wins
total = 0			#No of attempts
isStopped = True	#is Stopwatch not running?

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(ticker):
    # Minutes -> "//" interger floor division
    A = ticker // 600
    # Tenth of a minite
    B = ticker % 600 // 100
    # Seconds
    C = ticker % 100 // 10 
    # Tenth of a second
    D = ticker % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D) 

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global isStopped
    #start the stop watch
    isStopped = False
    timer.start()
    
    
def Stop():
    # stops timer and increments success and attempt counters
    global ticker, total, wins, isStopped
    if isStopped == False:
        total += 1
        if ticker % 10 == 0:
            wins += 1
    isStopped = True
    timer.stop()

def Reset():
    # stops timer, resets timer and counters to zero
    global ticker, total, wins, isStopped
    timer.stop()
    ticker = 0
    total = 0
    wins = 0   
    isStopped = True

def Quit():
    timer.stop()
    frame.stop()  


# define event handler for timer with 0.1 sec interval
def time_handler():
    global ticker
    ticker += 1

    
# define draw handler
def draw_stopwatch(canvas):
    canvas.draw_text(format(ticker), [width/4, height/2.5], width/6, "White")
    canvas.draw_text(str(wins) + "/" + str(total), (width/1.70, height/5), width/15, "Red")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch game", width, height)
frame.set_canvas_background('Black')

# register event handlers
timer = simplegui.create_timer(interval, time_handler)
frame.set_draw_handler(draw_stopwatch)

#Buttons
label = frame.add_label("THE STOPWATCH GAME")
frame.add_button("Start", Start, btnSize)
frame.add_button("Stop", Stop, btnSize)
frame.add_button("Reset Game", Reset, btnSize)
label = frame.add_label("")
label = frame.add_label("")
label = frame.add_label("")
frame.add_button("Quit Game", Quit, btnSize)


# start frame
frame.start()
