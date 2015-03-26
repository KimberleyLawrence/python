def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2
    """line 5 was originally n + 2, but was asked to change the body of deserves_another 
    so that it always adds + 2 onto the output of one_good_turn"""