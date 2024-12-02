###### Fun Functions!!! Its Fun........ ########

'''
    Abstraction = gets rid of complexity 
    function is a phrase or word that represents an algorithm
        function can do stuff
        function can do stuff and return stuff
        function can do basically whatever you want*
        function can take stuff and do stuff with it
    To use a function you must
        1. define the function
        2. give it an algorithm 
        3. call the function
'''
# y=mx+b the slope intercept 
# step 1    def slopeIntercept(x):
# step 2        return m*x+b
# step 3    y = slopeIntercept(0)

# add some number   2+2 print out 4
def addTwo(a,b):
    print(a+b)

addTwo(2,2)
addTwo(17,84)
addTwo(87,26)
addTwo(-5,6.9231321315)
addTwo("4","4")
addTwo([1,2,3],[4,5,6])

#Why do we return information
# will you need this later?
c = addTwo(2,2)
print(c) #printing pit a print f(x), you get a None type

def addTwo(a,b):
    return a+b

c = addTwo(55,55)
print(c)

# check the user's input
backpack=["flower","sugar","oats","knife","liberator 1085x"]
# check if the input is within range
# check for a integer
def getItemFromBackpack():
    ui=input("which item ")
    goodInput = 0
    while not ui.isdigit():
        if ui.isdigit():
            if int(ui) in range(len(backpack)):
                goodInput=1
            else:
                ui = input("which item ")
        else:
            ui = input("which item ")
    return int(ui)

print(backpack[getItemFromBackpack()])


print("\n"*50)

'''
    x|y
    ---
    0|x**2+x+7
    1|
    2|
    3|
    4|

'''

def parabola(x):
    return x**2+x+7

print("x|y")
print("___")
for i in range (-5,25):
    print(f"{i}|{parabola(i)}")

# sqrt cubroot => x**(1/2) x**(1/3)
