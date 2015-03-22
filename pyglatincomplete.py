#variable used in line 12
pyg = 'ay'
# word to be entered by the user - word to convert into pig latin
original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    # places the original word into lowercase
    word = original.lower() 
    # picks the first letter of the word
    first = word[0] 
    #adds lowercase word, first letter and ay to the end of the word
    new_word = word + first + pyg 
    #prints character at placement number 1 to length of the variable
    new_word = new_word[1:len(new_word)] 
    # prints the pig latin word into the console
    print new_word
else:
    print 'empty'