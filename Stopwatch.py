# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
total_stops = 0
successful_stops = 0
stopwatch_running = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = 0
    BC = 0
    D = 0
    time = int(t)
    if time < 10:
        D = time
    elif  10 <= time < 100:
        D = time % 10
        BC = time/10
    elif time >= 100:
        D = time % 10
        BC = (time/10) % 60
        A = time/600
    if BC < 10:
        BC = "0" + str(BC)
  
        
            
    return str(A) + ":" + str(BC) + "."  + str(D)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global  stopwatch_running
    timer.start()
    stopwatch_running = True
    
def stop():
    global total_stops, successful_stops, stopwatch_running
#it stops only if the stopwatch is running this way
#And no stop added if the stop is pressed
    if stopwatch_running:
        timer.stop()
        stopwatch_running = False
        total_stops+=1
        if time % 10 == 0:
            successful_stops+=1
    
def reset():
    global time, total_stops, successful_stops, stopwatch_running 
    if stopwatch_running == False:
        time = 0
        total_stops = 0
        successful_stops = 0
        timer.stop()
    

# define event handler for timer with 0.1 sec interval
def timer():
    global time, total_stops, successful_stops, stopwatch_running 
    time+=1
#Timer runs up to 10 minutes after that it resets
    if time == 6000:
        timer.stop()
        time = 0
        total_stops = 0
        successful_stops = 0
        
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [130, 100], 20, "Red")
    canvas.draw_text( str(successful_stops) + "/" + str(total_stops) ,[230,30],30,"green")
# create frame
frame = simplegui.create_frame("Stop Watch", 300, 200, 300)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer) 
start_button = frame.add_button("Start", start, 200)
stop_button = frame.add_button("Stop", stop, 200)
reset_button = frame.add_button("Reset", reset, 200)
# start frame
frame.start()
#timer.start()
# Please remember to review the grading rubric
