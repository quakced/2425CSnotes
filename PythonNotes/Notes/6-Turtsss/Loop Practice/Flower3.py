import turtle as trtl
import random

painter = trtl.Turtle()
wn=trtl.Screen()
painter.speed(1)

def randomColor(turtleObj):
    R=random.random() #generate a decimal
    G=random.random()
    B=random.random()
    turtleObj.color(R,G,B)
    
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

def drawingPetals(numOfPetals,size):
    for eachPetal in range(numOfPetals):
        # if eachPetal%2==0:
        #     painter.color("blue")
        # else:
        #     painter.color("darkorchid")
        randomColor(painter)
        painter.right(360/numOfPetals) #arc angle
        painter.fd(size) #chord???
        painter.stamp()
 
while True:
    drawingPetals(18,30)   

wn.mainloop()