# setting the function break_words that requires one argument entitled 'stuff'
def break_words(stuff):
    """This function will break up words for us."""
    # setting words to be the split up string of text on any whitespaces/blanks (' ')
    # expect to return a list of words
    words = stuff.split(' ')
    return words

def sort_words(words):
	"""Sorts the words."""
	# setting the function sort_words to sort the words that are split from stuff; we 
	# now have a list of words that are in alphabetical order. Capitalized words go 
	# first.
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	# setting the function print_first_word to print the first word in a list
	# we pop will remove and return the item on the list specified in the parenthesis
	# in this case it is 0 so the 1st item on the list and remove it from list
	word = words.pop(0)
	# will print the first word in the list
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	# setting the function print_last_word as the printing the last word in the list
	# will also remove this last word from the list
	word = words.pop(2)
	print word 

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	# we are defining sort_sentence as a function with argument sentence 
	# that combines the previous functions we have already built. We are splitting up the 
	# words in the sentence and then returning the words that are sored by calling for the sort_words 
	# function
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""prints the first and last words of the sentence."""
	# defining the print_first_and_last function that takes in the argument 'sentence'
	# words will be defined as the split up sentence which should be a list of words
	words = break_words(sentence)
	# calling the function print_first_word
	print_first_word(words)
	# calling the function print_last_word 
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	# defining the print_first_and_last_sorted function that take in argument 'sentence'
	# setting words as the list of of words when calling the function sort_sentence. This 
	# should be a list of words that are alphabeticaly ordered
	words = sort_sentence(sentence)
	# calling the function print_first_word
	print_first_word(words)
	# calling the function print_last word
	print_last_word(words)
