import random

randomNumber = random.randint(1,10)
correctAns=False
while(not(correctAns)):
    x = int(input("Guess A Number 1-10!: "))
    if x > randomNumber:
         print("To High!")
    elif x < randomNumber:
        print("To Low")
    else:
        print("You got the number!")
        correctAns=True
