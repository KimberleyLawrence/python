start_list = [5, 3, 1, 2, 4]
square_list = []
#create a variable for each item in the start_list
for number in start_list:
        #need to create a variable for the variable you wish to put an operator ** on. 
    square = number**2
    #then append the square_list to include the square variable results
    square_list.append(square)
#then sort the list into number sequence
square_list.sort()

# Your code here!


print square_list