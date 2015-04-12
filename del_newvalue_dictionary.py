# key - animal_name : value - location 
zoo_animals = { 
    'Unicorn' : 'Cotton Candy House',
    'Sloth' : 'Rainforest Exhibit',
    'Bengal Tiger' : 'Jungle House',
    'Atlantic Puffin' : 'Arctic Exhibit',
    'Rockhopper Penguin' : 'Arctic Exhibit'
}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
#print zoo_animals.values() printzoo_animals.keys() this will show you just the values (R), or just the keys (L)
zoo_animals["Rockhopper Penguin"] = "Ice Factory"



print zoo_animals