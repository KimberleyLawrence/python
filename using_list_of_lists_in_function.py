n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
#define a function called flatten with an argument list
def flatten(lists):
    #create an empty list called results
    results = []
    # loop through the outer list with the first for loop
    for numbers in lists:
        #loop through the inner list with the second loop
        for item in numbers:
            #append the item to the results list
            results.append(item)
    #return results
    return results
        



print flatten(n)