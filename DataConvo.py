'''
    Data Types
        Primitive Data
            - boolean = True or False statement  aka Lights on or Lights off
                        This is the SMALLEST data type you could ever have
            - integers = whole number (+/-) 
            - float = decimal number ie 3.14 or -.25 or 0.0
                        3/4 -> 3 divided by 4 => 0.75
                        75% -> string value 
            - character = char = this a single ASCII value
                        'a'
        Non-Primitive Data
            - Sequence Data
                - String - sequence of data join together as one piece of data
                - List
                - Tuple
                - Dictionaries or HashMap or JSON
            - Objects and Classes
'''
############        STRINGS N STUFF   #######################

email = "lord.bander@evsck12.com"

#find the number of characters - finds the number of items in SEQUENCE
print(len(email))

#binary of a letter
print(bin(ord("l")))
#ord() returns the character on the ASCII
#bin() returns the binary string of the number

#chr() input a # and return a character from the ASCII chart
print(chr(97))

#substring or grab a portion of the string
username = email[0:10+1]
print(username)
first = username[0:4]
print(first)
last = username[6-1:]
print(last)

#                                       endCharacter That's not included
#               string[startCharacter : endCharacter]


################   NUMBERS n Stuff #############################
print(3/4)
print(type(3))   #type() returns the data type
print(type(3/4))
print(type(9/3))

print(1/3) #0.3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

print(1/3 + 1/3 +1/3)   #0.9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

#rounding -> truncating
# 1/3+1/3+1/3 = 1.0 but in reality 0.9 repeating

print(0.9999999999999999999999)
print(0.000000000000000000000000000000000001)



