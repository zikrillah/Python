def uname(name):
    print "Your name is: %s" % name

def gender(sex):
    print "You gender is %s ?" % sex

promt = "> "

print "Hey there what is your name?"
name = raw_input(promt)

print "What is you gender %s ?" % name
sex = raw_input(promt)

uname(name)
gender(sex)

print "\nWelcome %s and you said you gender is %s" % (name, sex)
print "Thanks for visited %s, see you next time..!!!" % name
