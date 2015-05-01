
def make_ocean():
    board = []
    #this just makes the loop repeat 5 times to create a column
    for column in range(5):
        #Column creates a list of "o" * 5
        column = ["O"]*5
        #append board with column answers
        board.append(column)
    return board
#for grid template
for row in board:
    #print row
    #OR
    #will print the letter out with spaces " " and join them together 
    print " ".join(row)

#below code prints rows. 
def print_board(board):
    for row in board:
        print row
       
board = make_ocean()  