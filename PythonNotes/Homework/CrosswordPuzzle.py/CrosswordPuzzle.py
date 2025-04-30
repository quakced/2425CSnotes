def importWords():
     return listOfWords

def importBoard():
     return board

def printBoard(board):
     pass

#Horizontal Search
def searchHorizontally(word,board):
     return
#Vertical Search
def searchVerically(word,board):
     return

def searchRightDiagonal(word,board):
     return

def searchLeftDiagonal(word,board):
     return
length=11
for r in range(length):
    line=""
    for c in range(length):
        cellNumber= f"{(r+c)*10+c:02}"
        row = int(cellNumber[0])
        col = int(cellNumber[1])
        line+=cellNumber
    print(line)
    length-=1
    
wordSearchBoard=Practice Word Search.xlsx()
#Heads up, for testing, you could comment out this line and set words=your own list
words=importWords()

print(f'''
      
Original Board
{printBoard(wordSearchBoard)}

''')

#TODO:  Between these two print statements, you will run all of your searches.


print(f'''
      
Answer Board
{printBoard(wordSearchBoard)}

''')