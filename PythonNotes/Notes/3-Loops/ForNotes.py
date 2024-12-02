##### FOR LOOPS #####

'''
    range() -> is a built in f(x)
    range(startValue,stopValue, *stepValue)

    for i in range(10): the range is actually a list 

    for eachItem in list: every for loop follows this logic
        1. for loops can do something x amount of times
        2. access each item from a list
'''
print(range(10))        #from 0 to the number
print(range(5,10))      #from 5 to 10 but not 10
print(range(0,10,2))    #from 0 to 10 step by 2 but not 10

# for localVariable in list:
for eachItem in range(0,10,2):
    print(eachItem)
#Must be an integer
#for eachItem in range(-100,100):
#    print(eachItem)

#printing 0.1 to 1.0

for eachItem in range(1,11):
    print(eachItem/10)

#for anyNameForAVariableHere in list:
for eachTurd in range(0,5):
    print(eachTurd)

#Typically the local var is called i,j,k x,y,z n,m

print()
classroomRoster=["Justin","Ish","Scott","Adian"]
studentFavClass=["Recess","CS","World History","Math"]
number=1
for eachName in classroomRoster:
    print(f"{number}. {eachName}")
    number+=1
    print(eachName)
print()
for i in range(len(classroomRoster)):
    #print out #. studentName
    print(f"{i+1}. {classroomRoster[i]}")
print()

#Accessing two different list at the exact same time

for i in range(len(classroomRoster)):
    print(f"{i+1}. {classroomRoster[i]} - {studentFavClass[i]}")

#This is possible because the list are parallel
#   parallel - same length and indeces are related

#Capitilze
for i in range(len(classroomRoster)):
    classroomRoster[i] = classroomRoster[i].upper()
print(classroomRoster)

# remove any spaces in the class

for i in range(len(studentFavClass)):
    studentFavClass[i] = studentFavClass[i].replace(" ","")
print(studentFavClass)

studentEmail=[]
for i in range(len(classroomRoster)):
    email = f"{classroomRoster[i]}.{studentFavClass[i]}@stu.evsck12.com"
    studentEmail.append(email)

print(studentEmail)

print("\n"*50)
#Count the amount of vowels in a name
name = "spongebob Squarepants"

vowelCount=0
for letter in name:
    if letter in "aeiou":
        vowelCount+=1
print(vowelCount)


name = "pippy long stockings"

import random
sometimesY = random.randint(0,1)  # generate random int btwn 0 and 1
vowelCount = 0
for letter in name:
    if sometimesY == 1:
        if letter in "aeiouy":
            vowelCount+=1
    else:
        if letter in"aeiou":
            vowelCount+=1
print(vowelCount)
