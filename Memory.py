# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
import random 

#Global variabales
deck = range(1,9)*2
exposed = [False]*16
x = 20
counter = 0
card_one = 0
card_two = 0

#Helper functions
#start a new game
def new_game():
    
    global state, deck, exposed, counter
    random.shuffle(deck)
    exposed = [False]*16
    state = 0
    counter = 0
    

# Handler for mouse click

def reset():
    #resets the game
    new_game()

def mouse_click(pos):
    #Revealing a card from the deck
    global exposed, deck, state, card_one, card_two, counter
    card_num = pos[0]/50
    if exposed[card_num] == False:
        exposed[card_num] = True
        if state == 0:
            state = 1
            card_one = card_num
        elif state == 1:
            state = 2
            card_two = card_num
            counter += 1
            if deck[card_one] == deck[card_two]:
                exposed[card_one] = True
                exposed[card_two] = True            
        else:
            state = 1
            if deck[card_one] != deck[card_two]:
                exposed[card_one] = False
                exposed[card_two] = False
            card_one = card_num
            
            
# Handler to draw on canvas
def draw(canvas):
    global x, deck_pos, exposed, counter
    for num in range(0,len(deck)):
        canvas.draw_text(str(deck[num]),[x+50*num,60],40,"White")
        if exposed[num] == False:
            canvas.draw_polygon([(num*50, 0),((num+1)*50, 0),((num+1)*50,100),(num*50,100) ], 2, 'Black', 'Green')
    turns.set_text(str(counter))

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", reset)
frame.set_mouseclick_handler(mouse_click)
frame.set_draw_handler(draw)
turns = frame.add_label('0',100)


# Start the frame animation
new_game()
frame.start()
