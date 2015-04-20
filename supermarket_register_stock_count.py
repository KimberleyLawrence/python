shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        # print the item first so you know what the details following are for in the print out.
        print item
        #total += item - this is incorrect - line 24 correct
        # if the item in the stock is greater than 0, then run following code
        if stock[item] > 0:
            # adds the price of the item to the total
            total += prices[item]
            #takes one item away from item in stock
            stock[item] -= 1 
    return total #important to use indentation, otherwise continues to loop on itself and not add in the next item