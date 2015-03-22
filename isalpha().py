print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("What's your name?")
if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"