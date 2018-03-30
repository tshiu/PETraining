from sys import exit

#defining the function that is entitled gold_room
def gold_room():
	print "This room is full of gold. How much do you take?"

	#setting the variable next to the raw input that should answer the question before
	next = str(raw_input("> "))
	# Is the string is recognized as a number, then we will set the variable how_much to 
	# the integer value of the raw_input earlier added
	if next.isdigit() == True:
		how_much = int(next)

	# If the string does not contain a 1 or a 0, we will assume that this is not a number and 
	# they will be dead. This calls the dead function that is later defined.
	else:
		dead("Man, learn to type a number.")

	#if the integer that is set in how_much is less than 50, then we will print that the user has won 
	#and we will exit the game	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

#defining the function that is entitled bear_room 
def bear_room():
	"""User enters bear room and will navigate outcome based on input"""
	#print the following lines
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	print "Do you 'take honey' or 'taunt bear'?"
	#setting the variable bear_moved to false 
	bear_moved = False 

	#this remains true, we set next as the raw input
	while True:
		next = raw_input("> ")

		#if raw_input = take honey, then we will call the dead function with the following parameter
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		#if user types in 'taunt bear' and bear_moved is True, then we call the gold_room function
		# next == "taunt bear" (T) AND not False (T); this exits the loop since this is a while true function
		elif next == "taunt bear" and not bear_moved:
			gold_room()
		#otherwise, we print this function, I have no idea waht that means and it will go back to 
		#true
		else:
			print "I got no idea what that means."

#defining the function, ctulhu_room
def ctulhu_room():
	"""User enters ctulhu room and will navigate outcome based on input"""
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	#the variable next will be set as the raw input to the question posed
	next = raw_input("> ")

	#if the word flee is in next, then we will call the start function
	if "flee" in next:
		start()
	#If the word head is in next, then we will call the dead function
	elif "head" in next:
		dead("Well that was tasty!")
	#In all other cases, we will go back to the beginning of the function
	else:
		ctulhu_room()

def fly_away():
	"""User sprouts wings and flies away"""
	print "You sprout wings and start to fly away."
	print "You see a window or a vent, which path do you take?"
	route = raw_input("> ")

	if "window" in route:
		dead("A vulture eats you.")
	elif "vent" in route:
		gold_room()
	else:
		dead("That was not an option.")
#defining the function dead that accepts the parameter why
def dead(why):
	"""User dies; game ends with reason printed"""
	#will print the parameter in the why function followed by "good job"
	print why, "Good job!"
	#exit the game
	exit(0)

#defining the function start
def start():
	"""We begin the game at the beginning of the dark room"""
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take? left, right, or up?"

	#will set next to the raw_input that is in response to the posed question
	next = raw_input("> ")

	#if user writes left, we  will call the function bear room
	if next == "left":
		bear_room()
	#if user writes right, we will call the function bear room
	elif next == "right": 
		ctulhu_room()
	#if user write anything else, then we will call the dead function with the specified
	#parameter
	elif next == "up":
		fly_away()
	else:
		dead("You stumble around the room until you starve.")

#calling the start of the function
start()

#SD
#1. Map/List
#2. Yep!
#3. Added comments and doc comments
#4. Added an additional function
#5. Changed
