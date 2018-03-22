#print the below string that should prompt user to either enter in 1 or 2; should note
#that if they enter in #1 or #2, that will lead them to the last else statement
print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

#prompting user to set door as the input
door = raw_input("> ")

#if the user types in 1, then the below three strings/lines will be printed
if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	#expect the user to interpret the strings and enter in the relevant number
	#associated with the line. 
	#if the user does not enter in a recognized value, then 
	bear = raw_input("> ")

	#if the user inputs 1, then the below string will print and the script will end
	if bear == "1":
		print "The bear eats your face off. Good job!"
	#if the user input 2, then the below string will print and the script will end
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	#if the user does not input either 1 or 2, (i.e. if the above two statements are
	#recognized as false), then this else statement will print that places the input
	#the user entered into the string as a called variable and the script ends
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

#If the user types in 2, after the intiial prompt ("You enter a dark room with two doors, etc."
#then the below four strings will be printed)
elif door == "2":
	print "You stare into the endless abyss at Ctulhu's retina. What do you see?"
	print "1. Bluberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	#expect the user to interpret the above strings and to input the relevant information
	insanity = raw_input("> ")

	#If the user input either 1 or 2, they will be presented with the below string and script
	#will end
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	#if the user does not input either 1 or 2, they will be presented with the below string.
	#this else: line is a catch all for all the other values insanity can be set as
	elif insanity == "3":
		print "Which of the below options best describes the melodies you hear? Enter 1, 2, or 3."
		print "1. Kesha"
		print "2. Baby Metal"
		print "3. Justin Bieber"

		melody = raw_input("> ")
		
		if melody == "1":
			print "Awesome! Which song? Enter 1, 2, or 3."
			print "1. Praying"
			print "2. Tik Tok"
			print "3. Timber"

			kesha_song = raw_input("> ")
			
			if kesha_song == "1": 
				print "Topical...but Timber was the only right answer. You die."
			elif kesha_song == "2":
				print "Classic...but Timber was the only right answer. You die."
			elif kesha_song == "3":
				print "You win! That is the best Kesha song. You escape the bear."
			else: " %s is not a song worth mentioning." % kesha_song

		elif melody == "2":
			print "Not familiar with any of their songs, sadly. Good on you though!"
		elif melody == "3":
			print "Biebs is great, but I was really looking for Kesha. You die."
		else: 
			print "You cannot follow instructions. You die."	

	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

#If the user does not type in either 1 or 2 to the initial prompt, they will be presented with
#the below string
else:
	print "You stumble around and fall on a knife and die. Good job!"


#SD 
#1. Added a couple of additions to the above code. 