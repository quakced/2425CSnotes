#imports
import Car

#global var and objects
myCar = Car.Car("Murica","Tank","2026","Platnium")
ferd = Car.Car("Ford","F550","2025","Blue")
pinewood = Car.Car("Boy Scout","BlockOfWood","1990")

#f(x)

#mainloop
print(myCar.make)
print(myCar.model)
print(myCar.description())

myCar.make = "ford"
myCar.model = "Mustang"

print(myCar.description())

myGarage = [myCar,ferd,pinewood]
print(myGarage)
for eachCar in myGarage:
    print(eachCar.description())