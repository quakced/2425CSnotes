#############  MODEL  ################
#imports
import turtle
import math

#global variables or instantiate objects
#creating a tutle object
mikey = turtle.Turtle()     #turtlemodule.turtleConstructor()
mikey.shape('turtle')
mikey.speed(0)
mikey.color('blue')
wn = turtle.Screen()        #creating the window for your turtle

############# CONTROL  ################
#function / events

#mainloop
'''
    When you are working with objects
        objects have characteristics/properties - adjectives
        objects have methods/actions - verbs
    
    noun.verb or object.method() 
    noun.verb(directObjects) or object.method(object)
'''
for i in range(4):
    mikey.forward(50)  #50 units
    mikey.right(90)  #90 degrees

mikey.fd(25)  #fd is forward
mikey.circle(80)

mikey.teleport(25,-50)  #moves the turtle and has pen up
#mikey.goto(25,-50)  #moves the turtle and keeps the pen down
mikey.circle(-80)

mikey.penup()
mikey.goto(50,-25)
mikey.pendown()

mikey.fd(50*math.sqrt(2))
mikey.lt(135)
mikey.fd(50)
mikey.lt(135-45)
mikey.fd(50)

#############  VIEW  ################
wn.mainloop()                     ###!!!!!! MUST BE THE LAST LINE OF CODE!!!!!!!!!!


# MVC - Model View Controller - method to organize code for GUI
# GUI - Graphical User Interface