favoriteDrink = input(f"What is your favorite drink? ")
drinkNumber = 100
drinkNumber2 = 99
drink = (f"{drinkNumber} bottles of {favoriteDrink} on the wall {drinkNumber} bottles of {favoriteDrink}. Take one down and pass it around, {drinkNumber2} bottles of {favoriteDrink} on the wall.")
drink2 = (f"No more bottles of {favoriteDrink} on the wall, no more bottles of {favoriteDrink} on the wall. Go to the store and buy some more, {drinkNumber} bottles of {favoriteDrink} on the wall.")

while(drinkNumber!=0):
    print(f"{drinkNumber-1} bottles of {favoriteDrink} on the wall {drinkNumber-1} bottles of {favoriteDrink}. Take one down pass it around, {drinkNumber2} bottles of {favoriteDrink} on the wall.")
    drinkNumber-=1
    drinkNumber2-=1
else:
    print(drink2)

