n = [3, 5, 7]
# Add your function here
#define a function called list_extender with one parameter called lst
def list_extender(lst):
    #inside the function append the number 9 to lst
    lst.append(9)
    #return modified lst
    return lst

print list_extender(n)