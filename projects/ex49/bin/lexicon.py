direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verb = ['go', 'kill', 'eat']
stop = ['the', 'in', 'of']
noun = ['bear', 'princess']


def scanner(word):

	word = word.lower()

	if word in directions:
		return ('direction', word)
	elif word in verbs:
		return ('verb', word)
	elif word in stops:
		return ('stop', word)
	elif word in nouns:
		return ('noun', word)
	elif word.isdigit():
		return ('number', word)
	#else:
		#return ('error', word)

	#print "Hello World"

def break_sentence(sentence):
	
	words = sentence.split()

	tuples = []

	for word in words:
		#print scanner(word)
		tuples.append(scanner(word))

	return tuples

	#for word in words:
		#return scanner(word)
