import turtle as t

mikey=t.Turtle()

wn=t.Screen()
mikey.hideturtle()
wn.bgcolor('red')
wn.setup(width=600, height=600)
mikey.speed(10)



#middle yellow
mikey.teleport(300,-50)
mikey.right(45)
mikey.fillcolor('yellow')
mikey.begin_fill()
for i in range(2):
    mikey.forward(200)
    mikey.left(90)
    mikey.forward(600)
    mikey.left(90)

mikey.end_fill()

#star
mikey.begin_fill()
mikey.color('black')
mikey.teleport(50,0)


mikey.left(45)
mikey.forward(50)
mikey.left(150)
mikey.forward(50)
mikey.right(75)
mikey.forward(50)
mikey.left(150)
mikey.forward(50)
mikey.right(70)
mikey.forward(50)
mikey.left(140)
mikey.forward(50)
mikey.right(70)
mikey.forward(50)
mikey.left(150)
mikey.forward(50)
mikey.right(72)
mikey.forward(50)
mikey.left(150)
mikey.forward(50)

mikey.end_fill()


# bottom green


wn.mainloop()