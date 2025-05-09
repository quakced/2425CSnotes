#check for first time using the program
import random
from Input import Input
from User import User
from Entry import Entry
import csv
result=""
genPassword=""
passList=[]
masterUserList=[]
masterCategoryList=[]
masterEntryList=[]
s=7
    
    
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
# modify account info        
def modify():
    global first, last
    found = False
    updated_data =[]
    user=Input.getCorrectInput(["y","n"],"Would you like to modify your account information?(y/n) ")
    if user =="y":
        username = input("username: ")
        password = input("Password: ")
        with open("data.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 4 and row[0] == username and row[1] == password:
                        found = True
                        first = row[2]
                        last = row[3]
                        print("You are in!")
                        print("what would you like to modify (firstname, lastname, username, password). If you don't want to modify a certain thing just leave it how it was. ")
                        newusername = input("Newusername: ")
                        newPassword = input("Newpassword: ")
                        newfirst = input("New First name: ")
                        newlast = input("New last name: ")
                        confirmusername = input("confirm your username: ")
                        confirmpassword = input("confrim your password: ")
                        confirmfirst = input("confirm your first name: ")
                        confirmlast = input("confirm your last name: ")
                        if newusername != confirmusername and newPassword != confirmpassword and newfirst != confirmfirst and newlast != confirmlast:
                            print("The creditionals do not match...")
                            return
                        first = row[2]
                        last = row[3]
                        updated_data.append([newusername, newPassword, first, last])
                    else:
                        updated_data.append(row)
        if not found:
            print("Current credtials not found.")
        with open("data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_data)
        print("Credientials updated successfully")
    if user == "n":
        database()
        
#starting point of code asking to login or register
def login():
    global first, last  # So they can be used in createEntry, etc.
    user = Input.getCorrectInput(["login", "register"], "Login or Register? (login/register) ")

    if user == "register":
        print("Registration")
        username = input("What do you want your username to be? ")
        password = input("What is your password going to be? ")
        first = input("What is your first name? ")
        last = input("What is your last name? ")

        with open("data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password, first, last])
        print("Registration successful! Please log in.")
        login()

    elif user == "login":
        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            print("Login")
            username = input("Username: ")
            password = input("Password: ")

            with open("data.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 4 and row[0] == username and row[1] == password:
                        first = row[2]
                        last = row[3]
                        print("You are logged in!")
                        database()
                        return

            attempts += 1
            print(f"Incorrect credentials. Attempts left: {max_attempts - attempts}")

        print("Too many failed attempts. Exiting program.")
        quit()

def database():
    while True:
        print("1. Add a new Account")
        print("2. Generate Password")
        print("3. View Password")
        print("4. Categories")
        print("5. Create Entry")
        print("6. Modify account")
        print("7. Logout")
        answer = input("What would you like to do? ")

        if answer == "1":
            login()
        elif answer == "2":
            generatePW()
            print(f"Generated password: {passList[-1]}")
        elif answer == "3":
            viewPassword()
        elif answer == "4":
            getCategories()
        elif answer == "5":
            createEntry()
        elif answer == "6":
            modify()
        elif answer == "7":
            print("Logging out.")
            login()
            
        else:
            print("Invalid option. Please choose again.")
            database()
login()
