#imports section
import turtle as t
import time
#global car or objects or game configurations
delay=0.1

wn = t.Screen()
wn.bgcolor("grey")
wn.setup(width=600,height=600)

head=t.Turtle(shape="square")
head.speed(0)
head.penup()
head.direction="stop"

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
    head.direction="up"
#MOVE DOWN
def down():
    head.direction="down"
#move left
def left():
    head.direction="left"
#move right
def right():
    head.direction="right"
#game over

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


#mainloop
while True:
    wn.update()
    #check for collision(wall, food, body)
    # wall colision
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()>290 or head.xcor()<-290:
        head.teleport(0,0)
        head.direction="stop"
    move()
    time.sleep(delay)
wn.mainloop()