inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
#create a new key "pocket" in inventory, and make a list 
inventory['pocket'] = ["seashell", "strange berry", "lint"]
#sort backpack - as backpack is in inventory, you need to include it
inventory['backpack'].sort()
#remove 'dagger' from backpack -  remember it is in the inventory
inventory['backpack'].remove('dagger')
#add 50 to the number in the 'gold' key
inventory['gold'] = inventory['gold'] +50