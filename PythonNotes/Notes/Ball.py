import turtle as t
import random as r
COURT_HEIGHT=600
COURT_WIDTH=1000

wn=t.Screen()
wn.setup(width=COURT_WIDTH+100,height=COURT_HEIGHT+100)
wn.bgcolor(0.25,0.25,0.25)

ball=t.Turtle(shape="turtle")
ball.color("ivory")
ball.penup()
ball.speed(0)

def resetBall():
    ball.setpos(0,0)
    if r.randint(0,1)==0:
        ball.seth(r.randint(-30,30))
    else:
        ball.seth(r.randint(150,210))
def moveTheBall():                     #while(conditional statement)
    ball.fd(20)
    x,y=ball.position()
    if y>=COURT_HEIGHT/2 or y<=-COURT_HEIGHT/2:
        ball.seth(-ball.heading())
    if x>=COURT_WIDTH/2 or x<=-COURT_WIDTH/2:
        resetBall()
    wn.ontimer(moveTheBall,20)

wn.onkeypress(resetBall,"r")
wn.listen()

    
moveTheBall()
wn.mainloop()