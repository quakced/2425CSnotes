import turtle as t
import random as r

#ALL CAP VAR means constant and doesn't change
COURT_HEIGHT=980
COURT_WIDTH=1820
leftPoints,rightPoints=0,0
fontSettings=("Arial",80,"bold")

wn=t.Screen()
wn.setup(width=COURT_WIDTH+100,height=COURT_HEIGHT+100)
wn.bgcolor(.25,.25,.25)
print(t.screensize())
wn.tracer(1)

ball = t.Turtle(shape="turtle")
ball.color("ivory")
ball.penup()
ball.speed(0)

#left player or player blue/player
leftPlayer = t.Turtle("square")
leftPlayer.color("blue")
leftPlayer.penup()
leftPlayer.speed(0)
leftPlayer.turtlesize(4,1)                   #turtlesize will stretch the turtle
leftPlayer.setx(-COURT_WIDTH/2+10)
if leftPlayer>=COURT_HEIGHT/2 or leftPlayer<=-COURT_HEIGHT/2:             #check for top or bottom wall collision
        leftPlayer.seth(-leftPlayer.heading())

lScore = t.Turtle(visible=False)
lScore.color("blue")
lScore.speed(0)
lScore.teleport(-COURT_WIDTH/4,COURT_HEIGHT/4)  #place the score in the top left area of the court
lScore.write(leftPoints,font=fontSettings)

#right player or player orange
rightPlayer = t.Turtle("square")
rightPlayer.color("orange")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.turtlesize(4,1)                   #turtlesize will stretch the turtle
rightPlayer.setx(COURT_WIDTH/2-10)
if rightPlayer>=COURT_HEIGHT/2 or rightPlayer<=-COURT_HEIGHT/2:             #check for top or bottom wall collision
        rightPlayer.seth(-rightPlayer.heading())

rScore = t.Turtle(visible=False)
rScore.color("orange")
rScore.speed(0)
rScore.teleport(COURT_WIDTH/4,COURT_HEIGHT/4)  #place the score in the top left area of the court
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
    
def moveTheBall():                                      #while(conditional statement)
    global leftPoints,rightPoints
    ball.fd(20)                                             #do portion
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
        resetBall()                                         #   score a point
    else:
        collideWithPaddle(leftPlayer,ball)                  #check for paddle collision
        collideWithPaddle(rightPlayer,ball)
        
    wn.ontimer(moveTheBall,20)                              #iterator

def GameOver(lScore, rScore):
    PLAYER = leftPlayer or rightPlayer == int(7) 
    while True:
        if lScore or rScore == int(7):
            wn.color("green")
            wn.write(f"Game Over {PLAYER} Wins!")
            wn.onkeypress("space")
        break
GameOver()
def resetBall():
    ball.setpos(0,0)
    #flip a coin on who serves
    if r.randint(0,1)==0:
        ball.seth(r.randint(-30,30))  #random range to the right side of the screen
    else:
        ball.seth(r.randint(150,210)) #random range to the left side of the screen

def leftUp():                                   #TODO: stop it from going across the borders
    leftPlayer.sety(leftPlayer.ycor()+20)       #TODO: powerup???  slower or faster paddles?
def leftDown():
    leftPlayer.sety(leftPlayer.ycor()-20)

def collideWithPaddle(paddle,ball):
    #check for collision
    if paddle.distance(ball)<10:    #from snake...
        ball.seth(180-ball.heading())
        #to help prevent wall glitching
        if ball.xcor()>0:  #right paddle collision
            ball.setx(ball.xcor()-5)
        else:
            ball.setx(ball.xcor()+5)
        ball.fd(10)
    
def track_ball():
    if rightPlayer.ycor() < ball.ycor() and abs(rightPlayer.ycor() - ball.ycor()) > 10:
        rightPlayer.sety(rightPlayer.ycor() + 10)
    elif rightPlayer.ycor() > ball.ycor() and abs(rightPlayer.ycor() - ball.ycor()) > 10:
        rightPlayer.sety(rightPlayer.ycor() - 10)
    wn.ontimer(track_ball, 20)  # check every 20ms
def doublespeed(collideWidthPaddle,ball):
    if  collideWidthPaddle(r.randint(1,2)==2):
        ball.speed*2  
    else:
        ball.speed*1
#TODO: something to think about, only one key can run at a time
wn.onkeypress(resetBall,"r")
wn.onkeypress(leftUp,"w")
wn.onkeypress(leftDown,"s")
wn.onkeypress("space")
wn.listen()

#mainloop
drawCourt()
track_ball()
resetBall()
moveTheBall()
wn.mainloop()