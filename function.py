from variables import *

# These are all the functions for the game

# This function prints you characters stats.
def playerStat():
	print "%d health"       % playerHealth
	print "%d damage"	% playerDamage
	print "%d armor"	% playerArmor
	print "weapon: %s"	% playerWeapon


# This function lets you advanced when typing "next".
def next():
	next = raw_input("Type 'next' to continue: ")
	while next != "next":
		next = raw_input("Type 'next' to continue: ")


# This function equip an item. mostly for testing atm. this is the current command to equip, "playerDamage = equip("sword")"
def equip(item):
	if item == "dagger":
		return 15
	elif item == "sword":
		return 20


# This is a function to let you look at an item in the game.
def look ():
	global advance
	advance = 3
	while advance != 1 or 2:
		look = raw_input("Type 'look' to look at %s, or 'walk' to walk away: " % thing)
		if look == "look":
			advance = 1
		elif look == "walk":
			advance = 2
		elif look != "walk" or "look":
			advance = 3
		
		# This prints out your results and ends the while loop.
		if advance == 1:
			print "You look at %s " % thing
			break
		elif advance == 2:
			print "You walk away"
			break
		

# This is a function for picking up an item.
def pickup():
	advance = 3
	while advance != 1 or 2:
		pickup = raw_input("Do you wish to pick up %s? 'yes' or 'no': " % thing)
		if pickup == "yes":
			advance = 1
		elif pickup == "no":
			advance = 2
		elif pickup != "yes" or "no":
			advance = 3
			
		# this prints your results and ends the while loop.
		if advance == 1:
			print "You pick up %s" % thing
			break
		elif advance == 2:
			break
