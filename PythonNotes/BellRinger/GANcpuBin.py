import random
import sys

lo, hi=-sys.maxsize-1,sys.maxsize
secretNumber = random.randint(lo,hi)
compGuess = (hi+lo)//2
numGuess = 0
while(compGuess != secretNumber):
    if compGuess < secretNumber:
        print(f"{compGuess} is to low")
        lo = compGuess
    else:
        print(f"{compGuess} is to high")
        hi =compGuess

    compGuess = (hi+lo)//2
    numGuess+=1

print(f"You got the number in {numGuess} tries")
print(f"Secret number {secretNumber}")
