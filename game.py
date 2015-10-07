# Amma make a game!
from function import *
from variables import *


# Title
print "This is a game"
print " "
playerName = raw_input("What is your name? ")
print "Welcome to this world, %s." % playerName
print " "

next()

print " "
print "This is a world of chaos. Infested with orcs. It is your quest to stop them."
print " "

next()

print " "
print "Here is your initial stats:"
playerStat()

print " "
print "Good luck."

next()

thing = "shiny metal object"

print " "
print "You look out into the wilderness that is this world."
print "You see a %s on the ground." % thing
print " "

look()

if advance == 1:
	print "the shiny metal object is a dagger."
	print "Do you wish to pick it up?"
	#add function for picking up thing
elif advance == 2:
	print "you continue to walk, wondering on what that item might've been."

print "last message in game.py, if this showes, the game is ended"
