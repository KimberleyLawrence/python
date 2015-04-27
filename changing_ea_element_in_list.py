n = [3, 5, 7]
def double_list(x):
    # don't forget to make sure everything within the loop is attached to the function.
    for i in range(0, len(x)):
        x[i] = x[i] * 2
# Don't forget to return your new list!
    return x
    
    
print double_list(n)