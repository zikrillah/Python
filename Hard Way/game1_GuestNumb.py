from sys import exit
import random

def guess_number(name):
    guesesTaken = 0
    number = random.randint(1, 20)
    print "Well %s, I am thinking of a number between 1 and 20" % name

    while True:
	gueses = int(raw_input("> "))
	guesesTaken += 1

	if gueses < number:
	    print "Your guess is too low."

	elif gueses > number:
	    print "Yout guess is too hight."
	
	elif gueses == number:
	    win(name, guesesTaken)
	    break

	else:
	    print "Plese type the number."

def mulai():
    player = raw_input("What is your name: ")
    player_name = player.capitalize() #Set first letter to capitalize

    print "\nWelcome to guest number game %s" % player_name
    ready = raw_input("Are you ready to play the game (y/n)? ")

    if "Y" in ready or "y" in ready:
	print ready
	guess_number(player_name)
    else:
	print "Bey!!"
	exit(0)

def win(name, atempt):
    print "Conratulation %s !! you guessed my number in %d guesses!" % (name, atempt)

mulai()
