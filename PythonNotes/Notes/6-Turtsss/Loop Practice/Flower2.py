import turtle as trtl

painter = trtl.Turtle()
wn=trtl.Screen()
painter.speed(0)
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
        painter.right(360/numOfPetals)
        painter.fd(30)
        painter.stamp()
    
drawingPetals(18,30)

painter.color("blue")
painter.goto(20,180-30)
drawingPetals(12,30)

painter.color("yellow")
painter.goto(20,180-50)
drawingPetals(6,30)

wn.mainloop()
