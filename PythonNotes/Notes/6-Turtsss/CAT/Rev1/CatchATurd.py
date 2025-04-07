#imports
import turtle as t
import random as r
import Leaderboard as lb
import time
from sklearn.metrics import accuracy_score
#---global var and objects and game configuration

wn = t.Screen()
wn.screensize(600,600)
#wn.bgpic("turtle.gif")

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
    global timer
    print(f"m was clicked{mouseX},{mouseY}")
    movem()
    updateScore()
def addtime():
    global timer
    if mClicked:
        timer+=0.5
    else:
        updateTimer()

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
        m.speed(5)
        m.goto(1000,1000)
        manageLeaderBoard()
        print(manageLeaderBoard)
    else:
        timeKeeper.write(f"Time: {timer}",font=fontSetup)
    # to run constantly - recursion to keep the timer running
    #hey timekeeper, make the screen you are in, tick again in 1000ms
    
def manageLeaderBoard():#game over update
    global score
    hsNames = lb.getNames("db.txt")
    hsScores = lb.getScores("db.txt")
    if score > int(hsScores[-1]):
        currentName = input("Congrats, you made the leader board!\n\tEnter your name: ")
        lb.updateLeaderboard("db.txt", hsNames, hsScores,currentName, score)
        
    lb.drawLeaderboard(False, hsNames, hsScores, scoreKeeper,score)

def changebkgcolor():
    if mClicked == m:
        wn.bgcolor(r.randint(red, black, white))

def shrink():
    if mClicked:
        m.shapesize/2
    elif mClicked>=3:
        m.shapesize*2*3
shrink()

# Accuracy


while True:    #Turtle has "clock" widget built in
    timeKeeper.getscreen().ontimer(updateTimer,interval)
    wn.ontimer(updateTimer,interval)
    updateTimer()
    time.sleep(1)



#---events - event handlers
    m.onclick(mClicked)

#---mainloop
    movem()
    manageLeaderBoard()
    changebkgcolor()
    wn.mainloop()



'''
    Features List:
        1. Click a turd
        2. Turd move randomly
        3. Score
        4. Timer
        5. High Score rev1 or tomorrow
'''
