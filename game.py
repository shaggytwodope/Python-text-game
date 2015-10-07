# These are the main variables for the game

# Names and initial stats
playerHealth	= 100
playerDamage	= 10
playerArmor	= 0
playerWeapon	= "none"
thing		= "none"
advance		= 0
playerBag	= "none"

# These are all the functions for the game

# This function prints you characters stats.
def playerStat():
	print "%d health"       	% playerHealth
	print "%d damage"		% playerDamage
	print "%d armor"		% playerArmor
	print "weapon: %s"		% playerWeapon
	print "inventory: %s"		% playerBag


# This function lets you advanced when typing "next".
def next():
	next = raw_input("Type 'next' to continue: ")
	while next != "next":
		next = raw_input("Type 'next' to continue: ")


# This function equip an item. mostly for testing atm. this is the current command to equip, "playerDamage = equip("sword")"
def equip(item):
	if item == "dagger":
		global playerWeapon
		playerWeapon = "dagger"
		global playerDamage
		return 15
	elif item == "sword":
		playerWeapon = "sword"
		return 20


# This will ask you to equip thing, followed by equip function.
def askEquip():
	global advance
	advance = 3
	while advance != 1 or 2:
		askEquip = raw_input("Do you wish to equip %s? 'yes' or 'no': " % thing)
		if askEquip == "yes":
			advance = 1
		elif askEquip == "no":
			advance = 2
		elif askEquip != "no" or "yes":
			advance = 3
			
		# this prints results and ends the while loop
		if advance == 1:
			print "You equiped the %s" % thing
			equip(thing)
			print playerStat()
			break
		if advance == 2:
			print "you store it in your backpack for later"
			playerBag = thing
			print "inventory: %s"		% playerBag
			break

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
	global advance
	advance = 3
	while advance != 1 or 2:
		pickup = raw_input("Do you wish to pick up the %s? 'yes' or 'no': " % thing)
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
			
			# Amma make a game!


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
	thing = "dagger"
	print "the shiny metal object is a %s. " % thing
	pickup()
	if advance == 1:
		askEquip()
elif advance == 2:
	print "you continue to walk, wondering on what that item might've been."

print "last message in game.py, if this showes, the game is ended"
