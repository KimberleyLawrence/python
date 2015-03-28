#prints 10
def biggest_number(*args):
    print max(args)
    return max(args)
#prints -5    
def smallest_number(*args):
    print min(args)
    return min(args)
#prints 10
def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)