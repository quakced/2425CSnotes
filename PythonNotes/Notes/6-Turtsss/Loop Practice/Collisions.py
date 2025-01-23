import turtle as trtl
# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
tloc = 50
for s in turtle_shapes:
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50
# TODO: move turtles across and down screen, stopping for collisions

#cat and dog are turtles
def checkForCollisions(cat,dog):
    #check the distance betweeen the two objects
    if(cat.xcor()-dog.xcor() in range(-5,5)): # if no magnitude, range needs direction
      if(abs(cat.ycor()-dog.ycor() in range(5))): #absolute val is getting magnitude
        cat.color("grey")
        dog.color("grey")
        #if that are "touching" stop them
for step in range(50):
    for i in range(len(vert_turtles)): 
      if vert_turtles[i].fillcolor() != "grey":
        vert_turtles[i].fd(10)
        horiz_turtles[i].fd(10)
        checkForCollisions(horiz_turtles[i], vert_turtles[i])
        
	# do something
wn = trtl.Screen()
wn.mainloop()

'''
  Collision Algorithms
    -Hit Box - MIT
    -AB BA collisions - Lua Pong
    -Distance formula detection - Turtles
    
    -Computer Science Majors will study the algorithms
    -Software Developers will use the algorithms
    -Software Engineers will build the algorithms (physic module)
    
'''