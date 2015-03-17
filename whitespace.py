# whitespace not used correctly will create an error (line3-4)
def spam():
eggs = 12
return eggs
        
print spam()



# whitespace corrected


def spam():
    eggs = 12
    return eggs
        
print spam()