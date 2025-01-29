import turtle as t

wn=t.Screen()

timeKeeper = t.Turtle()
timeKeeper.ht()

timer=5
interval=1000
fontSetup = ("Times New Roman", 30, "normal")

def updateTimer():
    global timer
    timer-=1
    timeKeeper.clear()
    if timer<=0:
        timeKeeper.write("Time is up!",font=fontSetup)
    else:
        timeKeeper.write(f"Time: {timer}",font=fontSetup)
    # to run constantly - recursion to keep the timer running
    #hey timekeeper, make the screen you are in, tick again in 1000ms
    timeKeeper.getscreen().ontimer(updateTimer,interval)
    
#while True:    Turtle has "clock" widget built in
#    updateTmer()
#    time.sleep(1)


wn.ontimer(updateTimer,interval)

wn.mainloop()