#import statements

#global var
gameBoard=[[" "," "," "],
          [" "," "," "],
          [" "," "," "]]

#functions
def printboard(board):
     for row in range(3):
          print(f"{board[row][0]}|{board[row][1]}|{board[row][2]}")
          if row!=2:
               print("-"*5)
     print()
def checkForWinner(board):
    #row checker checker(horizontal checker)
    for r in range(len(board)):
        if(board[r][0]==board[r][1] and board[r][1]==board[r][2] and board[r][0]!=" "):
            print("winner winner chicken strip dinner")
            printboard(board)
            return True
    #vertical Checker
    for r in range(len(board)):
        if(board[0][r]==board[1][r] and board[1][r]==board[2][r] and board[0][r]!=" "):
            print("winner winner chicken strip dinner")
            printboard(board)
            return True
    #diagonal checker
    for r in range(len(board)):
        if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0]!= " "):
            if(board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0]!=" "):
                print("winner winner chicken strip dinner")
            printboard(board)
            return True
    return False
     
def checkForCAT(board):
     #CAT or Tie or Scratch
     # if there are no more " " in each row
     for row in board:
          if " " in row:
               return False
     return True

def userTurn():
     pass

def spotIsTaken(symbol,board,row,col):
     if board[row][col] == " ":
          board[row][col]=symbol
          return False
     return True
def ai(row, symbol, col, board):
    if spotIsTaken([2][2] or [0][0] or [2][0] or [0][2]):
         symbol="O"
         row=int(input(1))
         col=int(input(1))
         

#main loop
print("Welcome to Tic Tac Toe!")

symbol="X"
#keep looping until a winner if found or a tie
while(symbol!="Q"):
     #print the gameBoard
     printboard(gameBoard)
     
     #player take a turn
     goodSpot=False      #goodSpot will determine if valid input and spot not taken
     while not goodSpot:
          row=int(input("row: "))-1
          col=int(input("col: "))-1
          if row in range(3) and col in range(3):
               #check if spot taken
               if spotIsTaken(symbol,gameBoard,row,col):
                    print("Spot Taken")
               else:
                    goodSpot=True       #this will break the loop
     
     #check for a winner or CAT
     if checkForWinner(gameBoard) or checkForCAT(gameBoard):
          symbol="Q"
     
     #swap turns
     if symbol=="X":
          symbol="O"
          print("O's turn")
     elif symbol=="O":
          symbol="X"
          print("X's turn")
        
        
