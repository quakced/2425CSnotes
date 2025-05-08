class firsttime: 
    firstTime = input("Is this your first time using the program? (yes/no) ")
    if firstTime =="yes":
        print("Welcome! Please type a username, password, your first name, and your last name!")
        username = input("Input your username: ")
        password = input("Input your password: ")
        firstName = input("Input your firstname: ")
        lastName = input("Input your lastname:")

    elif firstTime =="no":
        print("Welcome back! Please login.")