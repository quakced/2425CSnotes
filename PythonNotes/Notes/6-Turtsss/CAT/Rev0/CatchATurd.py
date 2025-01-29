#imports
import turtle as t
import random as r

#---global var and objects and game configuration

wn = t.Screen()
wn.bgcolor("black")
wn.screensize(600,600)

m = t.Turtle(shape ="turtle")
m.shapesize(2)
m.fillcolor("aquamarine")
m.speed(5)
m.color("aquamarine")

scoreKeeper = t.Turtle()
scoreKeeper.teleport(200,300)
scoreKeeper.speed(0)
scoreKeeper.ht()
scoreKeeper.color("pink")

timeKeeper = t.Turtle()
timeKeeper.ht()
timeKeeper.color("goldenrod3")
timeKeeper.teleport(-200,315)

timer=5
interval=1000
fontSetup = ("Times New Roman", 30, "normal")
score=0

#---f(x)
def mClicked(mouseX,mouseY): # add an features to this f(x) that trigger when m is clicked
    print(f"m was clicked{mouseX},{mouseY}")
    movem()
    updateScore()

def movem():
    m.stamp()
    newX=r.randint(-290,290)
    newY=r.randint(-290,200)
    m.goto(newX,newY)

def updateScore():
    global score
    score+=1
    print(score)
    scoreKeeper.clear()
    scoreKeeper.write(f"Score: {score}", font=("Times New Roman",30,"normal")) 

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
    
#while True:    Turtle has "clock" widget built in
#    updateTmer()
#    time.sleep(1)
timeKeeper.getscreen().ontimer(updateTimer,interval)
wn.ontimer(updateTimer,interval)


#---events - event handlers
m.onclick(mClicked)

#---mainloop
wn.mainloop()



'''
    Features List:
        1. Click a turd
        2. Turd move randomly
        3. Score
        4. Timer
        5. High Score rev1 or tomorrow
'''