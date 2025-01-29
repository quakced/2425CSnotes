#BuffaloPlaid.py
import turtle

mikey=turtle.Turtle()
wn=turtle.Screen()

numOfSquares=0
for i in range(8):
    for r in range(8):
        print(f"{i}],{r}")
        if numOfSquares&2==r:
            mikey.color("red")
        elif numOfSquares&2==i:
            mikey.color("black")
         
        numOfSquares+=1
        mikey.stamp(shape = "square")

wn.mainloop()