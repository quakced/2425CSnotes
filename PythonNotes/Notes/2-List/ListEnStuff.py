'''
    Data Types
        int - whole numbers
        bool - T or F
        float - decimal numbers

        str - sequence of data
        list - sequence of data - you can store any data type
                                inside of one variable
'''

intList = [0,1,2,3,4,5,6,7,8,9]
groceryList = ["Pickles","Milk","Eggs","Cosmic Browie"]
mixedList = ["H",3,"11o"," ",["Wo","rl","d"]]

student = "bob"
student2 = "riley"
student3 = "Adian"
students = ["bob","sally","suzzie",student2,student3]
# Since there are multiple students, you make the bar plural 

empty=[]

print(student)

email="bob@gmail.com"
username = email[:3]
print(username)

print(f"first student is {students[0]}")

print(students[:3])
print(f"last student is {students[-1]}")
print(students[-3])

print("\n"*50) # not pro code, but clears the terminal
######## List Functions ###########
numbers=[1,4,6,7.2,5,5.5,5.5555555555555,0, -3.14]

##### Getting the basic stats #####################
print(f"amount of numbers: {len(numbers)}")
print(f"total of the numbers: {sum(numbers)}")
print(f"min of the numbers: {min(numbers)}")
print(f"max of the numbers: {max(numbers)}")
print(f"ave of the numbersL {sum(numbers) / len (numbers)}")


print("\n"*50)
######## add items to a list
backpack = []
backpack.append("Physics Textbook") #add item to a list
backpack.append("Notebook")
backpack.append("Chromebook")
backpack.append("Illegal Wireless communication Device")
#append adds to the end of the list


######## show items in a list
print(backpack)
print()


####### update items to a list
backpack[0] = "Calculus Textbook"


######### delete items from a list
del backpack[1] 
item = backpack.pop()# grabs the last item
item = backpack.pop(1) # grab the index 1 item

#removes an item from the list and returns the item
print(item)

print()
print(backpack)

backpack=[] #removes all items from a list

