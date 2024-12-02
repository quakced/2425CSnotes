#Print out 0-9
#i = 0
#while(i!=10):
#while(i<10):
#while(i<=9):
    #print(i)
    #i+=1
''' 
    While loops run until boolean expression is false
        Real life:
            -While my pos != target, step forward
            -While mouth is full, no eat more
            _While underwater, don't breathe
            -While light==red, don't go
        Programming Usage
            -Keeping the program running
            -Keep asking question
            -List out items
            -Count numbers
'''

'''
#iterator variable
ui = input("Guess what!? ")
#while boolean expression == True
while(ui!="WHAT!"):
    #do this

    #iterate the iterator variable
    ui = input("Guess what? ")
print("turkey butt")
'''
#print 9-0
#print 0-20 evens
#print 0-20 odds
#print 0-50 every 5 number
#print alphabet utilizing ASCII chart
#print -10 to 10 evens


#0-9
h = 0
while(h!=10):
    print(h)
    h+=1
#evens
r = 0
while(r!=20):
    print(r)
    r+=2
#0dds
i = 1
while(i<=20):
    print(i)
    i+=2
#0-50 every 5
i=0 
while(i!=50):
    print(i)
    i+=5

#print alphabet
i=65
while(i<=90):
    print(chr(i))
    i+=1
import string
print(string.ascii_uppercase)
i=0
while(i!=len(string.ascii_uppercase)):
    print(string.ascii_uppercase[i])
    i+=1
#print -10 to 10 evens
i=-10
while(i<=10):
    print(i)
    i+=2

