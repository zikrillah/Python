from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "So your script is %s with first variable is %s second is %s third variable is %s ." % (script, first, second, third)

script = raw_input("The script is called?")
first = raw_input("Your first variable is?")
second = raw_input("Your second variable is?")
third = raw_input("Your third variable is?")

print "So your script is %s with first variable is %s second is %s third variable is %s ." % (script, first, second, third)
