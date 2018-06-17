directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'kill', 'eat']
stops = ['the', 'in', 'of']
nouns = ['bear', 'princess']


def scanner(word):

	word = word.lower()

	if word in directions:
		return ('direction', word)
	elif word in verbs:
		return ('verbs', word)
	elif word in stops:
		return ('stops', word)
	elif word in nouns:
		return ('noun', word)
	elif word.isdigit():
		return ('number', word)
	#else:
		#return ('error', word)

	print "Hello World"

def break_sentence(sentence):
	
	words = sentence.split()

	tuples = []

	for word in words:
		#print scanner(word)
		tuples.append(scanner(word))

	return tuples

	#for word in words:
		#return scanner(word)
