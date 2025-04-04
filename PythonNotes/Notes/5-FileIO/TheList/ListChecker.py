#import section

#global var
'''
    mode is what are you doing with the file?
    r - reading
    w - writing
    a - appending
    w+ - create and write
'''

#f(x)
#csv -comma separated values
def display_list():
    #read in the text file
    #with openTool(filename,mode) as alias
    with open("TheList.csv","r") as file:
        #output to the terminal the data
        for eachLine in file:
            # print eachLine without \n on right end
            print(eachLine.rstrip())

#print out how many coal and toys we need
def count_items():
    toys,coal=0,0
    #read the text file
    with open("TheList.csv","r")as file:
        for eachLine in file:
            #look at 2nd piece of data
            # two var = eachLine w/0 \n are splite based on", "
            name,gift = eachLine.rstrip().split(", ")
            data = eachLine.rstrip().split(", ")
            #add to toys or coal if that value present
            if gift == "toy":
                toys+=1
            else:
                coal+=1
            #puke results to termainal
        print(f"""
    Toys: {toys}
    Coal: {coal}
        """)

def add_to_list():
    name = input("Name: ")
    gift = input("toy or coal ").lower()

    #open TheList.csv by appending to it alias is file 
    with open("TheList.csv","a") as file:
        lineToWrite = f"{name}, {gift}\n"
        #file write this string
        file.write(lineToWrite)
        print("{name} was added!")


def change_name():
    #obtain the old name and new name
    old = input("Current name: ")
    new = input("New Name: ")

    #read in all the data aka save the file to a list
    with open("TheList.csv","r") as file:
        line = file.readlines()#converts file to list
        print(lines)
        print(lines[-1])
    # find the old name
    for i in range(len(lines)):
        name,gift = eachLine.strip().split(", ")
        if name == old:
            name = new
            newData = f"{name}, {gift}"
            lines[i] = newData
    #reset the old to the new aka overwrite the file
    with open("TheList.csv","w") as file:
        for eachLine in lines:
            file.write(eachLine)
#main loop
while True:
    print("\n--- Santa's Nice and Naughty List ---")
    print("1. Display the list")
    print("2. Add a person to the list")
    print("3. Count toys and coal")
    print("4. Change Name")
    print("5. Exit")
    choice = input("Choose an option (1-5): ").strip()
                                                            
    if choice == "1":
        display_list()
    elif choice == "2":
        add_to_list()
    elif choice == "3":
        count_items()
    elif choice == "4":
        change_name()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
