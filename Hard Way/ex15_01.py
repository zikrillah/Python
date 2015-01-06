promt = "> "

print "Hello there, what is your name?"
name = raw_input(promt)
print "Do you want to open a file?"
openfile = raw_input(promt)
print "Type name of file that you want: "
filename = raw_input(promt)

txt = open(filename)
print "You ask me to open file %s \n" % filename
print txt.read()

print "File name: ", txt.name
print "Opening mode: ", txt.mode
print "Did file closed: ", txt.closed
print "\n"

txt.close()

print "Didi file closed: ", txt.closed
