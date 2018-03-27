from random import randint 
	
number = randint(0, 100)

#added a print here to debug
print number

#had to change the first modifer to int. Was previously setting it to str and it never
#matched up
guess = int(raw_input("What is your guess for a number between 1 and 100? \n"))

guess_taken = 1

while guess != number: 
	

	if guess < number: 
		print "A little higher..."
		
		
	elif guess > number: 
		print "A little lower..."

	else:
		break
		
	new_guess = int(raw_input("Lets try again. What's your guess? \n"))

	if new_guess == guess:
		print "That was the exact same guess. Try again."
		guess = int(raw_input("Lets try once more. Pick a different number \n"))
		#Why does setting new_guess to guess not work?
		#Answer: I had a type that was setting input to new_guess instead of guess
		new_guess = guess
		guess_taken = guess_taken + 1
		#These were included when I was troubleshooting what wasn't working
		#print "This is the if block"
		#print "This is the new_guess: %d " % new_guess
		#print "This is the number: %d " % number
		#print "This is the guess: %d " % guess


	elif new_guess != guess:
		guess = new_guess
		guess_taken = guess_taken + 1
		#print "this is the elif block"
		#print "The is the new_guess: %d " % new_guess
		#print "This is the number: %d " % number
		#print "This is the guess: %d " % guess



else:
	print "Yes, the number was %d! You win!" % guess
	print "You took %d guesses to get the answer. Not bad!" % guess_taken
		
		
		

		
		