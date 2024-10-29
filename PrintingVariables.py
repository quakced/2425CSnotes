print("We're printing some stuff")

# The "" represent a String data type

#anytime you run the input() the data from the user 
#       is a string data

name = input("What is your name? ")
#print(name)

'''
    VOCAB WORDS!
        Adstraction - removing the complexity
        Algorithms - set of instructions
        Concatenation - joining data together into a
            sequence data structure
'''
#  The + operator is concatenating the String data
print("Why hello " + name + "!")

#  Best practice is to not concatenate in a print()
#   You should utilize the print(f-String)
print(f"Why hello {name}!")

output = f"Why hello {name}!"
print(output)

story = f'''
    This is our epic story:
    A long long time ago....
    {name} was on an epic quest!...
'''
print(story)

time = input(f"What time did {name} wake up? ")

# concatenating a string to a previous variable
#  MIT -> story = story + time
story+= " "*4 + f"{name} woke up at {time}"
print(story)

'''
    Escape Characters - escape from normal text
    \t = tab
    \s = space for Java and JS
    \n = new line
    \' = '
    \\ = \
'''

print("#" + "#")
print("#"*2)
#print("#"/2) can't do this
#print("#"-"#") can't do this


#######  VARIABLE NAMING SYNTAX   ############
# This is a CONSTANT variable
SPEED_OF_LIGHT = 300000000
#speed_of_light = 300000000
SPEED_OF_SOUND = 
PI = 3.14
NEWYEAR = "JAN 1ST"
SCREEN_SIZE = 600
MY_SKILL_LEVEL = 0

#camelCase
camelCase = thisIsTheBest
#underscore_case
under_score = this_is_annoying








