#imports section
import turtle as t
import time
import random as r
#global car or objects or game configurations
delay=0.1
bodyParts=[]

wn = t.Screen()
wn.bgcolor("grey")
wn.setup(width=600,height=600)
wn.title("Snake2.0")

head=t.Turtle(shape="square")
head.speed(0)
head.penup()
head.direction="stop"

head2=t.Turtle(shape="square")
head2.speed(0)
head2.penup()
head2.direction="stop"


food = t.Turtle(shape="turtle")
food.speed(0)
food.penup()
food.teleport(100,100)
food.color("red")

#functions
def move():
    if head.direction == "up": # "up is us setting a string value"
        head.sety(head.ycor()+20)#reset the y value to be up 20 units
    elif head.direction == "down": 
        head.sety(head.ycor()-20)#reset the y value to be up 20 units
    elif head.direction == "left": 
        head.setx(head.xcor()-20)#reset the y value to be up 20 units
    elif head.direction == "right":
        head.setx(head.xcor()+20)#reset the y value to be up 20 units
#move()
#move up
def up():
    if head.direction!="down":
        head.direction="up"
#MOVE DOWN
def down():
    if head.direction!="up":
        head.direction="down"
#move left
def left():
    if head.direction!="right":
        head.direction="left"
#move right
def right():
    if head.direction!="left":
        head.direction="right"
#game over
def hideTheBodyParts():
    global bodyParts #Python cheat - where you tell the f(x) that is a global var
    head.teleport(0,0)
    head.direction="stop"
    for eachBodyPart in bodyParts:
        eachBodyPart.hideturtle()
    bodyParts=[]

#events - event handler - gold/yellow blocks from MIT
#event = when button clicked or when edge reached
#window.onkeypress(conmmand,"keyboard charcter") -google this some time
# command is a cunction without calling the function
# call the up() functionm you include the ()
# call the up command, you omit the()
wn.onkeypress(up,"w") # lowercase w... no need for shifting
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.listen()
#Pause
wn.onkeypress(pause,"p")
#unpause
wn.onkeypress(unpause,"o")
#Snake 2.0


#mainloop
while True:
    wn.update()
    #check for collision(wall, food, body)
    # wall colision
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()>290 or head.xcor()<-290:
        head.teleport(0,0)
        head.direction="stop"
        
    #food collision - distance 
    if head.distance(food) < 20:
        food.teleport(r.randint(-290,290), r.randint(-290,290))
        bodyPart=t.Turtle(shape="square")
        bodyPart.speed(0)
        bodyPart.penup()
        bodyParts.append(bodyPart)
        
    for i in range(len(bodyParts)-1,0,-1):
        newX=bodyParts[i-1].xcor()#get the x cooridnate of next bodyPart
        newY=bodyParts[i-1].ycor()#get the y cooridnate of next bodyPart
        bodyParts[i].teleport(newX,newY)
        
    #move the neck to head
    if len(bodyParts)>0:
        newX = head.xcor()
        newY = head.ycor()
        neck = bodyParts[0]
        neck.teleport(newX,newY)
        
        
    move()
    
    # check for body collision
    #if the head is within some distance of another bodyPart
    for eachBodyPart in bodyParts:
        if head.distance(eachBodyPart) < 10:
            hideTheBodyParts()
    time.sleep(delay)
#wn.mainloop() - again mainloop keeps the window open