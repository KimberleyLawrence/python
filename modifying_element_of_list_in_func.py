def list_function(x):
    #add three to the number at index 1, and store at index 1
    x[1] = x[1] + 3
    #return the list
    return x

n = [3, 5, 7]
print list_function(n)