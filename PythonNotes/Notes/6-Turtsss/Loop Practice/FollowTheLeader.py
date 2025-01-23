import turtle as trtl
# create an empty list of turtles
my_turtles = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

#add turtles to my_turtles
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  newColor=turtle_colors.pop()
  t.color(newColor)
  my_turtles.append(t)
 
startx = 0
starty = 0
direction=90
#moves the individual turtles
for t in my_turtles:
    t.teleport(startx, starty)
    t.setheading(direction)
    t.right(45)     
    t.forward(50)
  
    startx = t.xcor()
    starty = t.ycor()
    direction = t.heading()
#have the turtles move around the screen
while True:
  for i in range(len(my_turtles)):
    my_turtles[i].speed(10)
    
    #move the turtle to the next turtles's location
    #currentTurtle = nextTurtle's location
    nextX=my_turtles[i+1].xcor()
    nextY=my_turtles[i+1].ycor()
    my_turtles[i].teleport(nextX,nextY)
  
wn = trtl.Screen()
wn.mainloop()