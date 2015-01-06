from os.path import isfile

def create_a_file(filename):
    #Create a new file
    target = open(filename, 'w')
    print "Please insert a text: "
    sentence = raw_input('> ')

    #Write the sentence to file
    target.write(sentence)
    target.close()

print "What you wan to do?"
print """
1. Open file
2. Write a file
"""
choice = raw_input('> ')

if choice == "1":
    print "Please type youre file:"
    file_name_open = raw_input('> ')

    if isfile(file_name_open):
	print open(file_name_open).read()
	open(file_name_open).close()

    else:
	print "Sorry file your type doesn't exists"

elif choice == "2":
    print "Please type youre file name: "
    file_name_write = raw_input("> ")

    if isfile(file_name_write):
	print "File name exists, do you want to overwrite (Y/N)?"
	overwrite = raw_input('> ')

	if overwrite == "Y" or overwrite == "y":
	    create_a_file(file_name_write)

	else:
	    print "File not created"  
        
else:
    print "Bey!!"
