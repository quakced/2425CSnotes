'''
Boolean Experssions and Operators

    boolean - True and False
        operator - math functions +,-,*,/

            logic operations -
                    <        less than
                    >        greater than
                    <=       less than or equal
                    >=       greater than or equal to
                    ==       is it equal to
                    !=       is not equal to 
                    not      pythonic ! or opposite of the boolean exp to the right
                    and &&   both exp on both sides of the and is true
                    or ||    only one exp in either side of the or is true

 boolean expression is any combination of boolean values and logic operators
                                                                                        
                                                                                        '''


print(4 < 6)
print(4 < 7 and 3 > 1)

x=4
print x !=5)

print(True == False)
print(True != False)
print()

print(True and False)
print(True and True)
print()
print(True and False or True)
print(False or True and True)
print(True and True or False and True)

print()
print(bool(1)) #is ture
print(bool(0)) #is false
print(bool(0.5)) #is true
print(bool(-0)) 
print(True and 1 and 0)
print(1 and 0)
print(bool(1 and 0))

print()
print(bool("True"))

#### If IT IsS NOT 0 then it is true
### In most languages True is actually true
print()
print(7 =="7")
print("5" < "7")

# print(7 < "7") cannot compare because different data types
x = int(input("number: "))
if x == 7:
    print("You got the number")
elif (x > 7)
    print("to high")
else: (x < 7)
    print("to low")
##### CORRECT VERSION!!! #############
# If only 3 options, you should use an if elif else

x = int(input("number: "))
if x < 7:
    print("to low")
elif (x > 7)
    print("to high")
else: (x == 7)
    print("You got the number!")


