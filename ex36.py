from sys import exit

def lip_sync():
	print "Twist! Rupaul is allowing you to choose your song for a lip sync. What do you go for?"
	print "shut up and drive"
	print "roar"
	print "kitty girl"

	next = str(raw_input("> "))

	print next

	if next == "shut up and drive":
		sashay_away("This will never be better.")
	elif next == "roar":
		lip_sync_wig()
	elif next == "kitty girl":
		reveal()
	else:
		sashay_away("Wrong song.") 

def makeup():
	print "Which feature do you decide to enhance with your outfit?"
	print "lips"
	print "eyes"
	print "everything because this is drag!"

	next = raw_input("> ")
	if next == "lips":
		sashay_away("Lips is never the right answer. ")
	elif next == "eyes":
		snatch_game()
	elif next == "everything":
		shoes()
	else:
		sashay_away("Not an option.")

def shoes():
	print "Which shoes do you decide to go along with your pineapple gown?"
	print "stilts"
	print "ballet flats"
	print "stilletos"

	next = str(raw_input("> "))
	if next == "stilts":
		snatch_game()
	elif next == "flats":
		sashay_away("NEVER choose flats. ")
	elif next == "stilletos":
		lip_sync()
	else:
		print "Let's try that again..."
		shoes()

def snatch_game():
	print "Which icon would you like to impersonate for our beloved snatch game?"
	print "Miss Clio"
	print "Rupaul"
	print "Diana Ross"

	next = str(raw_input("> "))
	if next == "miss clio":
		sashay_away("Your accent sounds Irish.")
	elif next == "rupaul":
		sashay_away("Too much risk. ")
	elif next == "diana ross":
		lip_sync()
	else:
		print "Let's try that again..."
		snatch_game()

def lip_sync_wig():

	print "While you are dancing to Roar, your wig begins to shift."
	print "What do you do to save the performance: clip or throw the wig?"

	wig_fallen = False 

	while True:
		next = raw_input("> ")

		if next == "clip":
			sashay_away("Always just throw off the wig!")

		elif next == "throw" and not wig_fallen:
			reveal()

		else:
			print "I'm not sure what to make of that."	

def reveal():
	print "How many reveals do you have during the performance?"
	next = str(raw_input("> "))
	# If the string in next contains either 1 or 0, we will set the variable how_much
	# to the integer of next
	if next.isdigit() == True:
		how_much = int(next)

	# If the string does not contain a 1 or a 0, we will assume that this is not a number and 
	# they will be dead. This calls the dead function that is later defined.
	else:
		sashay_away("That was incorrect.") 

	if how_much < 10:
		sashay_away("Not enough reveals. Step it up next time.")
	else:
		print "Shantay, you stay! You are the epitome of charisma, uniqueness, nerve and talent." 
		exit(0)

def sashay_away(why):
	print why, "Please sashay away."
	exit(0)

def start():
	"""We begin this season 30 of Rupaul's Drag Race"""
	print "Welcome to Season 11 of Rupaul's Drag Race!"
	print "You must first decide on your debut outit."
	print "Which classic ensemble do you draw inspriation from?"
	print "Type the corresponding number."
	print "1. Raja's Carrie Chic Look"
	print "2. Manila's Pineapple Number"
	print "3. Violet Chachki's Plaid Reveal"

	next = int(raw_input("> "))

	if next == 1:
		makeup()
	elif next == 2: 
		shoes()
	elif next == 3:
		lip_sync()
	else:
		sashy_away("That was not an option. You are done before it begins. ")


start()

