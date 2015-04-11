animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")    # Use index() to find "duck"

print duck_index

# Your code here!
animals.insert(duck_index, "cobra")
"""originally had the number 2 in place of the duck index, this is correct, the code would work, but could create problems if inserting strings later - as it will only ever print the index[2] """

print animals # Observe what prints after the insert operation