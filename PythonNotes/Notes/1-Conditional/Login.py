#Conditionals = If something is true, then  something happens
'''
    Conditionls is usually the if then statements

    if something is true:
        do this

    if boolean expression is true:
        do this
'''

masterUsername = "admin"
masterPassword = "admin"

username = input("username: ")
password = input("password: ")

if username == masterUsername:
    print("username is correct")
    
'''
    else statments - trigger when everything else fails

'''

if username == masterUsername:
    print("username is correct")
else:
    print("username is not correct")

'''
    So far you only have 2 options 
        basically a yes or no question

    Mutiple options or else if
        else if -> elif
'''

if password == masterPassword:
    print("password is correct")
else:
    print("password is not corrct")
if username == masterUsername:
     print("username is correct")
elif username == masterPassword:
    print("username and password should not be tha same")
else:
     print("username is not correct")


'''
    Nested conditional Statments 
        Nested = code that is indented under another line of code

    if this is true:
        if this is true:
            then do this

    error: indetation is incorrect or indentation error
        check your tabs and indentation for each line of code

'''
if username == masterUsername:
    print("username is correct")
    if password == masterPassword:
        print("Welcome to the program")
    else:
        print("creditials are not correct")
else: 
    print("creditials are not correct")
'''
    Complex Conditonal Statemnts
        and -> checks if the boolean exp in both sides of the and statement equal true
        or -> checks if the boolean exp in both sides of the or is at least one true
'''
if username == masterUsername and password == masterPassword:
    print("Welcome to the program")
else:
    print("credentials are not correct")



