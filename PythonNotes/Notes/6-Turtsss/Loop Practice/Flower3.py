import turtle as trtl
import random

painter = trtl.Turtle()
wn=trtl.Screen()
painter.speed(0)

def randomColor():
    R=random.random()
    G=random.random()
    B=random.random()
    painter.color(R,G,B)
    
# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)
# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)
# draw flower
painter.color("darkorchid")
painter.goto(20,180)

def drawingPetals(numOfPetals):
    for eachpetal in range(numOfPetals):
        if eachpetal&2==0:
            painter.color("blue")
        else:
            painter.color("darkorchid")

        painter.right(360/numOfPetals)
        painter.fd(30)
        painter.stamp()
while True:    
    drawingPetals(18,30)

    painter.color("blue")
    painter.goto(20,180-30)
    drawingPetals(12,30)

    painter.color("yellow")
    painter.goto(20,180-50)
    drawingPetals(6,30)

    wn.mainloop()
