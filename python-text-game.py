# Amma make a game!


playerHealth	= 100
playerDamage	= 10
playerArmor	= 0
playerWeapon	= "none"
thing		= "none"

def next():
	next = raw_input("Type 'next' to continue: ")
	while next != "next":
		next = raw_input("Type 'next' to continue: ")
		
def playerStat():
	print "%d health"       % playerHealth
	print "%d damage"	% playerDamage
	print "%d armor"	% playerArmor
	print "weapon: %s"	% playerWeapon

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


