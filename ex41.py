#imporitng random module
import random
#importing the urlpopen module
from urllib import urlopen
import sys

#setting word_url to this string. When you navigate to this url, it is just
#a webage with a random list of words
WORD_URL = "http://learncodethehardway.org/words.txt"
#setting WORDS to an empty list
WORDS = []

#setting PHRASES to this empty dictionary 
PHRASES = {
	#this string will replace the %%% with random words generated from the word_URL and pulled into 
	#the words list
	#defining the relationships between the code structure and what it is when translated into English
	#the key is how it is written in code and the value is the in English format 
	"class %%%(%%%):":
		"Make a class named %%% that is a %%%",
	"class %%%(object):\n\tdef __init__(self,***)" :
		"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
		"class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
		"Set *** to an instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribtue and set it to '***'."
}

# do they want to drill phrases first
#setting the variable PHRASE_FIRST to False as default
PHRASE_FIRST = False
#if the system arg has two things (python code and "english"), then this will set PHRASE_FIRST and True
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True 

# load up the words from the website
#creating a for loop, for each word in the webpage with the words loaded, 
#the readlines()function will read the file and create a list with the words
for word in urlopen(WORD_URL).readlines():
	#this puts the word from the URL page that has been read and parsed into 
	#a list into the empty WORDS list that was defined before
	WORDS.append(word.strip())

#defining the convert function that takes the parameters snippet and phrase
def convert(snippet, phrase):
	#setting the variable class names to a the capitalized word in in the random sample 
	#of words and passing the word inside the snippet based on the count
	#this is only setting the class name so the word needs to be capitlized
	class_names = [w.capitalize() for w in 
					random.sample(WORDS, snippet.count("%%%"))]
	#setting the variable other_names to a word from the the list and snippet
	other_names = random.sample(WORDS, snippet.count("***"))
	#setting an empty list named results
	results = []
	#setting an empty list named params
	param_names = []

	#setting a for function
	#for every item in the range from  0 to the snippet count
	for i in range(0, snippet.count("@@@")):
		#param count is set from 1-3
		param_count = random.randint(1,3)
		#random.sample function will return the # of param_count of WORDS from
		#the list that we earlier created by parsing through the words in the URL
		#we are joining these WORDS with the , and appending them to the param names list
		param_names.append(', '.join(random.sample(WORDS, param_count)))
	#setting for function for every setence ins snippet 
	for sentence in snippet, phrase:
		#setting result to sentence[:] which is a copy of sentence
		result = sentence[:]

		# fake class names 
		#for word in the class_names list (set in line 53), we are replacining
		#the "%%%" placeholder with the word from the list, the last parameter 
		#1 states that only the first instance is replaced
		for word in class_names:
			result = result.replace("%%%", word, 1)

		# fake other names
		#same ckass names but with a different replacement value
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		#same as the fake class names 
		for word in param_names:
			result = result.replace("@@@", word, 1)
		#adding class_names, other_names, and param_names to the empty result list 
		#that was created before
		results.append(result)

	return results

# keep going until they hit CTRL-D
#setting a try function so that except will escape the function
try:
	while True:
		#setting snippets to key values in the PHRASES dictionary
		snippets = PHRASES.keys()
		#this will shuffle the snippets list and will pick a random item
		random.shuffle(snippets)
		#for each snippet (item) in the snippets list
		for snippet in snippets:
			#set phrase to a snippet from the PHRASES list
			phrase = PHRASES[snippet]
			#setting variables question and answer to snippet and phrase	
			#tried to look up the convert method and actually couldn't find documentation
			question, answer = convert(snippet, phrase)
			#if PHRASE_FIRST is true then we reverse the order of question and answer
			if PHRASE_FIRST:
				question, answer = answer, question 
		#print question
		print question 

		raw_input("> ")
		#print Answer
		print "ANSWER: %s\n\n" % answer
#if we receive the EORERRO (what happens when you press control D), then 
#end program
except EOFError: 
	print "\nBye"