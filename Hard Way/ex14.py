from sys import argv

script, user_name = argv
promt = "> "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name
likes = raw_input(promt)

print "Where do you live %s?" % user_name
lives = raw_input(promt)

print "What kind of computer do you have?"
computer = raw_input(promt)

print """
Alright, so you said %s about linking me.
You live in %s. Not sore where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer)
