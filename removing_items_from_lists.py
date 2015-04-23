n = [1, 3, 5]
# Remove the first item in the list here
#removes the item at index 0 from the list and returns it to you.
n.pop(0)
#will remove the actual item it finds - not the index, removes the number 1
n.remove(1)
#similar to .pop in that it will remove the item at the index, but wont return it
del(n[0])
print n