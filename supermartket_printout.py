prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
    }
    
stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15,
    }
for product in prices:
    #print the name of the product, then price, then stock
    print product
    print "price: %s" % prices[product]
    print "stock: %s" % stock[product]