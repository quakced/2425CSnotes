import random

botGuess = random.randint(1,10)
randomNumber = int(input("Input a random number from 1-10 that the Bot will guess: "))
while(botGuess != randomNumber):
    if botGuess > randomNumber:
         print(f"{botGuess} To High!")
    elif botGuess < randomNumber:
        print(f"{botGuess} To Low")
    else:
        print("The bot got your number!")
