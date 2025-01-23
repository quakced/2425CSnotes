#imports
import turtle
import math


#global variables or instantiate objects
# creating turtle
mikey = turtle.Turtle()
mikey.shape('turtle')
mikey.color('green')
mikey.speed(20)
wn = turtle.Screen()
mikey.fillcolor()
wn.setup(width=800, height=800)
wn.bgcolor('light blue')

t = turtle.Turtle()

#function / events

#mainloop

#tree
mikey.teleport(-125,0)
mikey.begin_fill()
for i in range(2):
    mikey.fd(200*math.sqrt(2))
    mikey.lt(135)
    mikey.fd(200)
    mikey.lt(135-45)
    mikey.fd(200)
    mikey.lt(135)
    mikey.teleport(-125,-140)
    
mikey.teleport(-125,140)
mikey.fd(200*math.sqrt(2))
mikey.lt(135)
mikey.fd(200)
mikey.lt(135-45)
mikey.fd(200)
mikey.lt(135)

mikey.end_fill()

#stump
mikey.begin_fill()
mikey.color('brown')
mikey.teleport(-10,-140)
mikey.right(90)

for i in range(2):
    mikey.forward(100)
    mikey.left(90)
    mikey.forward(50)
    mikey.left(90)

mikey.end_fill()

#star
mikey.begin_fill()
mikey.color('yellow')
mikey.teleport(15,285)


mikey.left(45)
mikey.forward(100)

mikey.left(150)
mikey.forward(100)
mikey.right(75)
mikey.forward(100)
mikey.left(150)
mikey.forward(100)
mikey.right(70)
mikey.forward(100)
mikey.left(140)
mikey.forward(100)
mikey.right(70)
mikey.forward(100)
mikey.left(150)
mikey.forward(100)
mikey.right(72)
mikey.forward(100)
mikey.left(145)
mikey.forward(100)

mikey.end_fill()

#snowman
mikey.begin_fill()
mikey.color('white')
#body
mikey.teleport(-300,0)
mikey.circle(80)
#bottom
mikey.teleport(-300,-130)
mikey.circle(100)
#HEAD
mikey.teleport(-300,120)
mikey.circle(60)
mikey.end_fill()
#eyes
mikey.color('black')
mikey.begin_fill()
mikey.teleport(-350,150)
mikey.circle(20)
mikey.teleport(-300,150)
mikey.circle(20)
mikey.end_fill()

#ornaments
#1
mikey.color('red')
mikey.begin_fill()
mikey.teleport(-75,-25)
mikey.circle(20)
mikey.end_fill()
#2
mikey.color('blue')
mikey.begin_fill()
mikey.teleport(100,120)
mikey.circle(20)
mikey.end_fill()
#3
mikey.color('purple')
mikey.begin_fill()
mikey.teleport(70,-100)
mikey.circle(20)
mikey.end_fill()

#text
t.teleport(0,450)
t.write("Christmas Turtle Post Card!", align="center",font=("Arial",16, "normal"))
t.hideturtle()

#image
#wn.register_shape(sleigh.jpg: )
#wn.addshape("sleigh.jpg")
#t.shape("sleigh.jpg")

#t.penup()
#t.goto(0, 0)
#t.pendown()

#moving snow
mikey.color('white')
mikey.begin_fill()
mikey.circle(20)
mikey.end_fill()









mikey.hideturtle()
turtle.exitonclick()
