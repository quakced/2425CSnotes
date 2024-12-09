import random

while True:
    botGuess = random.randint(1,10)
    randomNumber = int(input("Input a random number from 1-10 that the Bot will guess: "))
    while(botGuess != randomNumber):
        if botGuess > randomNumber:
            botGuess = random.randint(1,10)
            print(f"{botGuess} To High!")
        else:
            botGuess = random.randint(1,10)
            print(f"{botGuess} To Low")
        if botGuess == randomNumber:
            print("The bot got your number!")
