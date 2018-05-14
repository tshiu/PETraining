from sys import exit
from random import randint

class Round(object):

	def enter(self):
		print "This is the base class by which contestants will need to compete"
		exit(1)


class Engine(object):
	
	def __init__(self, round_map):
		self.round_map = round_map

	def play(self):
		
		current_round = self.round_map.opening_round()
		
		while True: 
			print "\n-------"
			
			next_round = current_round.enter()
	
			current_round = self.round_map.next_round(next_round)

class Eliminated(Round): 

	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a loser."
		"I have a small puppy that's better at this."
	]

	def enter(self):
		print Eliminated.quips[randint(0, len(self.quips)-1)]
		exit(1)

class MiniChallenge(Round):

	def enter(self):
		
		print "You have started out your drag career in NYC."
		print "Who is your go-to impersonation?"

		action = raw_input("> ") 

		if action == "Cher":
			print "Go to lipsync!"
			return 'sewing_room'

		elif action == "Madonna":
			print "Madonna is no longer relevant."
			return 'elimination_round'

		else:
			print "Sorry, there were only Cher and Madonna wigs left!"
			return 'mini_challenge'

class SewingRoom(Round):

	def enter(self):
		print "You have made it to the work room."
		print "How many stitches do you put in your bustier (1-20)?"
		stitches = "%d" % (randint(1,20))
		print stitches 
		guess = raw_input("> ")
		guesses = 0 

		while guess != stitches and guesses < 3:
			print "You had a wardrobe mulfunction! Repair it."
			guess = raw_input("How many stithces this time? \n> ")

		if guess == stitches: 
			print "Move on to the maxi challenge"
			return 'maxi_challenge'
	

class LipSync(Round):
	
	def enter(self):

		your_points = 10 
		brandons_points = 10 

		print "You have to lipsync against Brando."
		print "You have three attacks:"
		print "1. Death Drop"
		print "2. Jump Rope"
		print "3. Wig Snatch"
		print "Which of the above actions do you want to take?"
		action = str(raw_input("> "))

		if action == "Death Drop": 
			your_points = 10 - randint(1,3)
			brandons_points = 10 - randint(1,9)

		elif action == "Jump Rope":
			your_points = 10 - randint(1,4)
			brandons_points  = 10 - randint(1,7)

		elif action == 'Wig Snatch':
			your_points = 10 - randint(1,4)
			brandons_points = 10 - randint(1,7)

		else:
			print "You only have the above moves!"
			return lipsync

		while your_points > 0 and brandons_points  > 0:
			print "Your energy level is %r" % your_points
			print "Brandon's energy level is %r" % brandons_points  
			action = str(raw_input("> "))

			if action == "Death Drop": 
				your_points -= randint(1,3)
				brandons_points  -= randint(1,3)

			elif action == "Jump Rope":
				your_points -= randint(1,4)
				brandons_points  -= randint(1,5)

			elif action == 'Wig Snatch':
				your_points -= randint(1,4)
				brandons_points  -= randint(1,3)
			else:
				print "What? Try again"
				print "What is your next move?"	
				return lipsync

		if your_points < 1:
			print 'You ran out of breath'
			return 'elimination_round'

		elif brandons_points < 1:
			print "You beat Brandon. Amazing!"
			return 'winning'



class MaxiChallenge(Round):

	def enter(self):
		print "What color do you make your dress?"

		action = raw_input("> ")

		if action == "pink":
			print "Cute color, but Brandon also wore pink."
			return 'lipsync'

		elif action == "brown":
			print "Eew"
			return 'elimination_round'

		elif action == "black":
			print "yes"
			return 'winning'

		else: 
			print "They did not have that color fabric. There is only"
			print "brown, pink and black left."
			return "maxi_challenge"


class Winning(Round):

	def enter(self):
		print "You won! Good job."
		return 'finished'

class Map(object):
	
	rounds = {
		'lipsync': LipSync(),
		'sewing_room': SewingRoom(),
		'mini_challenge': MiniChallenge(),
		'maxi_challenge': MaxiChallenge(),
		'winning': Winning(),
		'elimination_round': Eliminated(),
	}

	def __init__(self, start_round):
		self.start_round = start_round

	def next_round(self, round_name):
		return Map.rounds.get(round_name)
	
	def opening_round(self):
		return self.next_round(self.start_round)

a_map = Map('mini_challenge')
a_game = Engine(a_map)

a_game.play()






























