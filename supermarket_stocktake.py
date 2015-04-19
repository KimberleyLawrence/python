prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for item in prices:
    print item
    print "price: %s" % prices[item]
    print "stock: %s" % stock[item]
    
total = 0
for item in prices:
    value = stock[item] * prices[item]
    total = total + value
    #have to remember to reassign the total variable to make sure it knows to add on value
print total
    