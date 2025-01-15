#import
 
 
#global var or objects
gameboard=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
] #this is a 2d list we can access each item
 
 # functions
 #print the board
'''
1|2|3
-----
4|5|6
-----
7|8|9

'''
def printBorad(board):
    for r in range(3):
        print(f"{board[r][0]}|{board[r][1]}|{board[r][2]}")
        if r != 2:
            print("-"*5)
 # check for winner
def checkForWinner(board):
    #row checker checker(horizontal checker)
    for r in range(len(board)):
        if(board[r][0]==board[r][1] and board[r][0]==board[r][2]):
            print("winner winner chicken strip dinner")
            print(board)
            return True
    #vertical Checker
    #diagonal checker
    return False
 #check for CAT
def checkForCAT(gamebaord):
    for eachRow in gameboard:
        if " " in eachRow:
            return False
    print("Yo dog, we have a CAT game!")
    return True
 #userTurn
 #Spot is taken
def spotIsTaken(symbol,board,row,col):
    if board[row][col] == " ":
        board[row][col]=symbol
        return False
    return True 
 #mainloop
symbol = "X"
while(symbol!="Q"):
    #print the board
    print(gameboard)
    #player will take a turn
    #keep asking until we have a validSpot
    vaildSpot=False
    while not vaildSpot:
        row = int(input("row: "))-1
        col = int(input("col: "))-1
        if row in range(3) and col in range(3):
            if spotIsTaken(symbol,gameboard,row,col):
                print("Spot Taken")
            else:
                vaildSpot=True
        
    gameboard[row][col]=symbol
    #check for winner or cat game2
    if checkForWinner(gameboard) or checkForCAT(gameboard):
        symbol = "Q"
    
    #swap turns
    if symbol == "X":
        symbol = "O"
    else:
        symbol = "X" 
    