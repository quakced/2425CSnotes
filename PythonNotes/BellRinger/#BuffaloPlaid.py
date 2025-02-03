#BuffaloPlaid.py
import turtle

mikey=turtle.Turtle()
wn=turtle.Screen()
mikey.hideturtle()
mikey.speed(20)

def drawSquares():
    mikey.begin_fill()
    for i in range(4):
        mikey.forward(50)
        mikey.left(90)
    mikey.end_fill()
drawSquares()
def drawRows():
    x=-200
    y=200
    for i in range(8):
        if(i% 2 == 0):
            mikey.color('red')
        else: 
            mikey.color('black')
        mikey.penup()
        mikey.goto(x,y)
        mikey.pendown()
        drawSquares()
        x+=50
drawRows()
def drawCol():
    x=-200
    y=200
    for i in range(8):
        if(i% 2 == 0):
            mikey.color('red')
        else: 
            mikey.color('black')
        mikey.penup()
        mikey.goto(x,y)
        mikey.pendown()
        drawSquares()
        y-=50
drawCol()
def drawboard():
    x=-150
    y=150
    for i in range(8):
        if i == 0:
            mikey.penup
            mikey.goto(x,y)
            mikey.teleport(-100,150)
            mikey.pendown
        drawCol()
drawboard()
#for i in range(8):
#    for r in range(8):
#        print(f"{i}],{r}")
#        if i &2==0:
#            mikey.color("red")
#        elif r &2==0:
#            mikey.color("black")

wn.mainloop()
