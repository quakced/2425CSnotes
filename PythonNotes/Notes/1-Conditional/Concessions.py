# iteration 1: Prder some popcorn
'''
    ask the user for what size popcorn
        small = $5
        med = $6
        large = $7
    print out their total
        subtotal: $_.__
'''
#Global Variables
subtotal = 0
order="User's Order\n"

popcorn = input('''
What size popcorn do you want?
       (s) Small = $5.00
       (m) Medium = $6.00
       (l) Large = $7.00
       (n) no popcorn
''')

if popcorn == "s":
    subtotal+=5
elif popcorn == "m":
    subtotal+=6
elif popcorn == "l":
    subtotal+=7
else:
    subtotal=0
order+=f"\t{popcorn} popcorn\n"
print(f"subtotal: ${subtotal:.2f}")
# iteration 2: Order a nice fresh soda pop
'''
    Ask the user for what size soda pop they would want
        small = $3.00
        med = $4.00
        large = $5.00
            ask if they wnat shild size for just $0.38 cents more 
    print out their current order and subtotal
        subtotal: $_.__

'''

SodaPop = input('''
What size SodaPop do you want?
       (s) Small = $3.00
       (m) Medium = $4.00
       (l) Large = $5.00
       (n) no Soda
''')
if SodaPop == "s":
    subtotal+=3
elif SodaPop == "m":
    subtotal+=4
elif SodaPop == "l":
    subtotal+=5
    child = input("Would you like a child size for only $0.38 more? (y/n)")
    if child == "y":
        subtotal+=0.38
        SodaPop = "c"
else:
    subtotal+=0

order+=f"\t{SodaPop} Soda Pop\n"
print(f"subtotal: ${subtotal:.2f}")

# iteration 3: What candy do you want?
'''
    What type of cnady would you like
        Sour Patch Kids $2.00
        M & M's         $2.50
            Plain
            Peanuts
            crunchy
        Licorish        $2.50
            Twizzlers
            Red Vines   
    print current order
    print the subtotal
'''

candy = input('''
What size Candy do you want?
       (s) Sour Patch Kids = $2.00
       (mpl) M & M's plain = $2.50
       (mpe) M & M's peanuts = $2.50
       (mc) M & M's crunchy = $2.50
       (lt) Licorish Twizzlers = $2.50
       (lv) Red Vines = $2.50
       (n) no Candy
''')
if candy == "s":
    subtotal+=2
elif candy == "mpl":
    subtotal+=2.50
elif candy == "mpe":
    subtotal+=2.50
elif candy == "mc":
    subtotal+=2.50
elif candy == "lt":
    subtotal+=2.50
elif candy == "lv":
    subtotal+=2.50
else: 
    subtotal+=0
order+=f"\t{candy} Candy\n"
print(f"Subtotal: ${subtotal:.2f}")

'''
if candy == "s":
    subtotal+=2
elif candy == "m" or candy == "l":
    subtotal+=2.50
    if candy == "m":
        candyType = input("(Pl}ain or (Pe)anuts or (C)runchy? ")
        candy = f"{candyType} M&M's"
    else:
        candyType = input("(T)wizzlers or (R)ed Vines? ")
        candy = f"{candyType} Licorish"
else:
    subtotal+=0

order+=f"\t{Candy} Candy\n"
print(order)
print(f"Subtotal: ${subtotal:.2f}")
'''
# iteration 4: Butter toppings do cost... sorry...
'''
    Ask the user for how many pumps of butter they need>
        Each pump = $0.25
    Print out the order
    Print out the subtotal
'''
butter = int(input("How many pumps ($0.25) of butter would you like? "))
if butter < 0:
    butter = 0

subtotal += butter * 0.25
order+=f"\t{butter} butter\n"
# subtotal:.2f means it will have 2 decimal places
print(f"Subtotal: ${subtotal:.2f}")
# iteration 5: If they ordered popcorn, soda, and candy give them $1,50 off
#                   Checkout with a tax of 7%
''' Final Output
        User's Order
            popcorn
            drink
            candy
            butter
            t/n for discount

            subtotal
            tax amount
            total
'''

if popcorn!="n" and SodaPop!="n" and candy!="n":
    subtotal -= 1.50
    order+= "\ty discount\n"
else:
    order+="\tn discount\n"

order+=f"\n\tsubtotal: ${subtotal:.2f}\n"
order+=f"\ttax:      ${subtotal*.07:.2f}\n"
subtotal*=1.07
order+=f"\ttotal:     ${subtotal:.2f}\n"
print(order)
