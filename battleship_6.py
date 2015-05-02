# import the randit function from the random module
from random import randint 

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# Add your code below!

def random_row(board):
    #creates a random row index
    board = randint(0,4)
    return board
    
def random_col(board):
    #creates a random column index => randit (0, length of the board - 1), same for above random_row
    board = randint(0,4)
    return board
