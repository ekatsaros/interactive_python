# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    
    
    global secret_number
    secret_number = random.randint(0,100)
    
    global num_of_guesses
    num_of_guesses = int(math.ceil(math.log(101,2)))
    #n holds number of guesses to keep track of the last played game
    global n 
    n = num_of_guesses
    
    
    
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    print "New game, Range is 0 to 100"
    
    new_game()
    
    global secret_number
    secret_number = random.randint(1,100)
    
    global num_of_guesses
    num_of_guesses = int(math.ceil(math.log(101,2)))
    #n holds number of guesses to keep track of the last play
    global n 
    n = num_of_guesses
    
    print "Number of Remaining Guesses is ", num_of_guesses
    print
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "New game, Range is 0 to 1000"
    new_game()
    
    global secret_number
    secret_number = random.randint(1,1000)
    
    global num_of_guesses
    num_of_guesses = int(math.ceil(math.log(1001,2)))
    #n holds number of guesses to keep track of the last play
    global n 
    n = num_of_guesses
    
    print "Number of Remaining Guesses is ", num_of_guesses
    print
    
    
    
def input_guess(guess):
    # main game logic goes here	
    
    guess = int(guess)
    
    global secret_number
    global num_of_guesses
    #n holds number of guesses to keep track of the last play
    global n
    
    num_of_guesses -= 1
    
    if num_of_guesses > 0:
       
        print "Guess was ", guess
        
      
        
        if guess > secret_number:
            print "lower."
            print "Number of Remaining Guesses is ", num_of_guesses
        elif guess < secret_number:
            print "higher."
            print "Number of Remaining Guesses is ", num_of_guesses
        else:
            print "Correct!"
            if n == 10:
                range1000()
            else:
                range100()
    
    else:
        print "You are out of guesses!"
        if n == 10:
            range1000()
        else:
            range100()
    print

    
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Enter a guess",input_guess, 200)
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
