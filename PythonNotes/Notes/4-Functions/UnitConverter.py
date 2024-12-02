#synchronous programming languages
#import modules and files
#from theFile import thisThing
from Conversion import *

#global variables/objects
menu = '''
    in to cm (ic)
    cm to in (ci)
    km to m (kgg)
    m to km (gkg)
    stop (quit)
'''

#define f(x)


#main loop
user = input(menu)
while(user!="quit"):
    if user == "ic":

        inches=float(input("How many inches? "))

print(in2cm(inches))
    elif user == "ci":
        pass
    elif user == "kmm":
        pass
    elif user == "mkm":
        pass
    else:
        print("I'm sorry I didn't quite get that")

    user = input(menu)
