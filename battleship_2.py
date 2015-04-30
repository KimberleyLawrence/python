
def make_ocean():
    board = []
    #this just makes the loop repeat 5 times to create a column
    for column in range(5):
        #Column creates a list of "o" * 5
        column = ["O"]*5
        #append board with column answers
        board.append(column)
    return board
    
       
       
board = make_ocean()  
