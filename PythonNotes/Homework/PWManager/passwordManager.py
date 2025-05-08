#check for first time using the program
import random
from Input import Input
from User import User
from Entry import Entry

result=""
genPassword=""
passList=[]
masterUserList=[]
masterCategoryList=[]
masterEntryList=[]
s=7
def database():
    global answer
    print("1. Add a new Account")
    print("2. Generate Password")
    print("3. Categories")
    print("4. view Password")
    print("5. Create Entry")
    print("6. Logout")
    answer = input("What would you like to do? ")
if answer == 1:
    
    
#generates password if called on to
def generatePW():
    newPassword=""
        

        #import all ascii numbers
    asciiNumbers = (33,35,36,37,38,40,41,42,48,49,50,51,52,53,54,55,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,94,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122)
        
    numCap = 1
    numLow = 5
    numNum = 2
    numSC = 1

    mixed = numCap + numLow + numNum + numSC 

    capitalLetters = (65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90)
    lowerLetters = (97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122)
    numbers=(48,49,50,51,52,53,54,55,56,57)
    specialCharacters=(33,35,36,37,38,40,41,42,64,94)
    while mixed != 0:
            newLetter = random.choice(asciiNumbers)
            if newLetter in capitalLetters:
                if numCap > 0:
                    numCap -= 1
                    newPassword += (chr(newLetter))
            elif newLetter in lowerLetters:
                if numLow > 0:
                    numLow -= 1
                    newPassword += (chr(newLetter))
            elif newLetter in numbers:
                if numNum > 0:
                    numNum -= 1
                    newPassword += (chr(newLetter))
            elif newLetter in specialCharacters:
                if numSC > 0:
                    numSC -= 1
                    newPassword += (chr(newLetter))
                    
            mixed = numCap + numLow + numNum + numSC 
    
    passList.append(newPassword)
   
#grabs categories and entries to display when called on      
def getCategories():
    global first,last
    file1 = open(f"{last}_{first}_entries.txt")
    file = file1.readlines()
    for line in file:
        account,username,password,category,lname,fname = line.rstrip().split(",")
        line = Entry(account,username,password,category,lname,fname)
        masterEntryList.append(line)
        masterCategoryList.append(category)
        
#allows user to see all entries including: account, username, password, category, etc.       
def viewPassword():
    for i in range(len(masterCategoryList)):
        print(masterCategoryList[i])
    user=Input.getCorrectInput(masterCategoryList,"Choose a category: ")
    for e in masterEntryList:
        if e.getCategory() == user:
            print(e)

#create an entry for anything
def createEntry():
    global first,last
    
    user=Input.getCorrectInput(["y","n"],"Would you like to create an entry?(y/n) ")
    if user =="y":
        account = input("Account(website): ")
        username = input("Username(for website): ")
        password = input("Password(for website): ")
        category = input("Category: ")
        masterCategoryList.append(category)
        newEntry = Entry(account,username,password,category,first,last)

        fileToWriteTo = open(f"{newEntry.getFileName()}","a")
        fileToWriteTo.write(newEntry.__str__())  #print does the __str__ for you -> write does not
        fileToWriteTo.close()
    elif user =="n":
        pass
            
#starting point of code asking to login or register
user=Input.getCorrectInput(["login","register"],"Login or Register? (login/register) ")
if user =="register":
    print("registration")
    with open("data.csv", "w") as file:
        username =input("What do you want your username to be? ")
        password =input("What is your password goint to be? ")
        firstname =input("What is your first name? ")
        lastname =input("What is your Last name? ")
        file.write (f"{username},{password},{firstname},{lastname}")
        
elif user =="login":
    print("login")
    with open("data.csv","r") as file:
        username =input("username: ")
        password =input("Password: ")
        firstname =input("First name: ")
        lastname =input("Last name: ")
        file.read (f"{username},{password},{firstname},{lastname}")
        data = file.read (f"{username},{password},{firstname},{lastname}")
    if data == True:
        print("You are logined in!")
    else:
        print("One or more user credentials are wrong...")
        username =input("username: ")
        password =input("Password: ")
        firstname =input("First name: ")
        lastname =input("Last name: ")


quit()