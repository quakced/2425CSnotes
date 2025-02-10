#def get_board(n):
    # get the numbers
#    numbers = [i for i in range(n * n)]

    # create the nested list representing the board
#    rev_board = [numbers[i:n+i][::+1] for i in range(0, len(numbers), n)]

#    return rev_board

#board = get_board(10)

#print('\n'.join(' '.join(str(x) for x in row) for row in (board)))
length=10
for r in range(length):
    line=""
    for c in range(length):
        cellNumber=f"{(r+c)*10+c:02} " # :02 forces 2 places
        # if you need the indeces cellNumber should be a string...
        line+=cellNumber
    print(line)
    length-=1