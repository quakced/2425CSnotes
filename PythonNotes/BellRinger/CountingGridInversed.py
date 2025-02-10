#    def print_grid(rows,cols):
#        for i in range(rows):
 #           for j in range(cols):
 #               print("%2d" % i,j,)
 #   rows=10
 ##   cols=10
 #   print_grid(rows,cols)

def get_board(n):
    # get the numbers
    numbers = [i for i in range(n * n)]

    # create the nested list representing the board
    rev_board = [numbers[i:n+i][::+1] for i in range(0, len(numbers), n)]

    return rev_board

board = get_board(10)

print('\n'.join(' '.join(str(x) for x in row) for row in (board)))
