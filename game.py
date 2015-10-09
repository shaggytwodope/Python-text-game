# Names and initial stats
playerHealth	= 100
playerDamage	= 10
playerArmor	= 0
playerWeapon	= "none"
thing		= "none"
playerBag	= "none"



# This function prints you characters stats.
def playerStat():
	print "%d health"       	% playerHealth
	print "%d damage"		% playerDamage
	print "%d armor"		% playerArmor
	print "weapon: %s"		% playerWeapon
	print "inventory: %s"		% playerBag


# Enemy Class
class enemy(object):
    def __init__(self):
	self.health(100)
    def hit(self,amount):
	self.health -= amount
    def getHealth(self):
	return self.health



# Combat function
def combat():
    askCombat = raw_input("Do you wish to 'attack' or attempt to 'flee'?: ")
    print ""
    while askCombat != "attack" or "flee":
	if askCombat == "attack":
	    print "You attack the enemy"
	    print ""
	    break
	elif askCombat == "flee":
	    print "You fled the enemy"
	    print ""
	    break


	

# This function lets you advanced when typing "next".
def next():
	next = raw_input("Type 'next' to continue: ")
	while next != "next":
		next = raw_input("Type 'next' to continue: ")


# This function equip an item. I should merge this and askEquip.
def equip(item):
	if item == "dagger":
		global playerWeapon
		playerWeapon = "dagger"
		return 15
	elif item == "sword":
		playerWeapon = "sword"
		return 20


# This will ask you to equip thing, followed by equip function.
def askEquip():
    askEquip = raw_input("Do you wish to equip %s? 'yes' or 'no': " % thing)
    while askEquip != "yes" or "no":
	if askEquip == "yes":
	    print "You equiped the %s" % thing
	    print ""
	    global playerDamage
	    playerDamage = equip(thing)
	    print playerStat()
	    print ""
	    break
	elif askEquip == "no":
	    print "You store it in your backback for later"
	    print ""
	    playerBag = thing
	    print "Inventory: %s" % thing
	    print ""
	    break


# This is a function to let you look at an item in the game.
def look ():
	global advance
	advance = 3
	while advance != 1 or 2:
		look = raw_input("Type 'look' to look at %s, or 'walk' to walk away: " % thing)
		print ""
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


combat()

print "last message in game.py, if this showes, the game is ended"


