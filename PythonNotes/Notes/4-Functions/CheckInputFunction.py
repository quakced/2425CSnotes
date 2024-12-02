question = "Check (y)es or (n)o "
correctAns = ["y","Y","n","N","Yes","yes","no","No","YES","NO"]

ui = input(question)

#while(ui!="y" and ui!="n"):
#    ui = input(question)

while(not(ui in correctAns)):
    ui = input(question)
#if you need to modify the data, do it now
print(ui)

def userInput(question,correctAns):
    ui=input(question)
    while(not(ui in correctAns)):
        ui = input(question)
    #clean the data here if you want
    return ui

answer = userInput("(t)urkey or (h)am ",["t","h","T","H"])
answer = input("turkey and hame")
print(answer)

