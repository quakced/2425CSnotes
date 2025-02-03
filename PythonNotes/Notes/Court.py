import turtle as t
import random as r

#ALL CAP VAR means constant and doesn't change
COURT_HEIGHT=600
COURT_WIDTH=1000
leftPoints,rightPoints=0,0
fontSettings=("Arial",80,"bold")

wn=t.Screen()
wn.setup(width=COURT_WIDTH+100,height=COURT_HEIGHT+100)
wn.bgcolor(.25,.25,.25)

ball = t.Turtle(shape="turtle")
ball.color("ivory")
ball.penup()
ball.speed(0)

#left player or player blue
leftPlayer = t.Turtle("square")
leftPlayer.color("blue")
leftPlayer.penup()
leftPlayer.speed(0)
leftPlayer.turtlesize(4,1)                   #turtlesize will stretch the turtle
leftPlayer.setx(-COURT_WIDTH/2+10)

lScore =t.Turtle(visible=False)
lScore.color("Blue")
lScore.speed(0)
lScore.teleport(-COURT_WIDTH/4,COURT_HEIGHT/4)
lScore.write(leftPoints,font=fontSettings)

#left player or player blue
rightPlayer = t.Turtle("square")
rightPlayer.color("orange")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.turtlesize(4,1)                   #turtlesize will stretch the turtle
rightPlayer.setx(COURT_WIDTH/2-10)

rScore =t.Turtle(visible=False)
rScore.color("Orange")
rScore.speed(0)
rScore.teleport(COURT_WIDTH/4,COURT_HEIGHT/4)
rScore.write(rightPoints,font=fontSettings)

def drawCourt():
    border=t.Turtle(visible=False)
    border.color("white")
    border.speed(0)
    border.penup()
    #top left corner
    border.setposition(-COURT_WIDTH/2,COURT_HEIGHT/2)
    border.pendown()
    border.fd(COURT_WIDTH)   #top right corner
    border.penup()
    
    border.sety(-COURT_HEIGHT/2)   #bottom right corner
    border.pendown()
    border.bk(COURT_WIDTH)    #bottom left corner
    
    border.setposition(0,-COURT_HEIGHT/2)  #bottom middle
    border.setheading(90)
    
    #dashes
    for i in range(COURT_HEIGHT//50):   #// divides without a decimal - int division
        border.fd(26)
        border.penup()
        border.fd(26)
        border.pendown()
    
def moveTheBall():  
    global leftPoints,rightPoints                            #while(conditional statement)
    ball.fd(20)                                             #do portiont
    x,y=ball.position()                                     #gets the x,y of ball
    if y>=COURT_HEIGHT/2 or y<=-COURT_HEIGHT/2:             #check for top or bottom wall collision
        ball.seth(-ball.heading())
    
    elif x>=COURT_WIDTH/2 or x<=-COURT_WIDTH/2:             #side wall collision = reset ball
        if x<-COURT_WIDTH/2:
            rightPoints+=1
            rScore.clear()
            rScore.write(rightPoints,font=fontSettings)
        else:
            leftPoints+=1
            lScore.clear()
            lScore.write(leftPoints,font=fontSettings)
        resetBall()
    else:
        collideWithPaddle(leftPlayer,ball)
        collideWithPaddle(rightPlayer,ball)
    wn.ontimer(moveTheBall,20)                              #iterator

def resetBall():
    ball.setpos(0,0)
    #flip a coin on who serves
    if r.randint(0,1)==0:
        ball.seth(r.randint(-30,30))  #random range to the right side of the screen
    else:
        ball.seth(r.randint(150,210)) #random range to the left side of the screen

def leftUp():
    leftPlayer.sety(leftPlayer.ycor()+20)
def leftDown():
    leftPlayer.sety(leftPlayer.ycor()-20)
def rightUp():
    rightPlayer.sety(rightPlayer.ycor()+20)
def rightDown():
    rightPlayer.sety(rightPlayer.ycor()-20)
    
def collideWithPaddle(paddle,ball):
    #check for collision
    if paddle.distance(ball)<20: # from snake..
        ball.seth(180-ball.heading())
        if ball.xcor()>0:
            ball.setx(ball.xcor()-5)
        else:
            ball.setx(ball.xcor()+5)
        ball.fd(10)

wn.onkeypress(leftUp,"w")
wn.onkeypress(leftDown,"s")
wn.onkeypress(rightUp,"Up")
wn.onkeypress(rightDown,"Down")
wn.onkeypress(resetBall,"r")
wn.listen()

drawCourt()
moveTheBall()
wn.mainloop()