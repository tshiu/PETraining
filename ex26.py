def break_words(stuff):
    """This function will break up words for us."""
    # The function break_words will split the words in a string by space
    words = stuff.split(' ')
    return words

def sort_words(words):
    """This function will sort the words in alphabetical order with capitalizations
    and spaces first."""
    # will return sorted words alphabetically
    return sorted(words)

def print_first_word(words):
    """This function will print the first word in a list and remove it from the list."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """This function will print the first word in al ist and remove it from the list."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """The function takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """This function rrints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """This function sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."

#Should escape the first two dashes and slash; will have a new line before 'new lines'
#and a tab before the word 'tabs'
print 'You\'d need to know \'bout escapes with \\ that do \nnew lines and \t tabs.'

#Will tab the first line,
#have a new line before 'the needs of love
#hae a new line and two tabs before the last line
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

# will pront the poem between the two lines
print "--------------"
print poem
print "--------------"

#adjusted the math to return 5 as it was previously returning six
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#defining the function secret_formula which accepts on argument entitled started
def secret_formula(started):
    #number of jelly_beans will be the intial number (started) *500
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    #this function will return three values
    return jelly_beans, jars, crates


start_point = 10000
#setting beans, jars, and crates as the values returned from the secret_formula function
beans, jars, crates = secret_formula(start_point)

#%d is a placeholder for a numerical value
print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

# this should return the above values divided by 10 
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


sentence = "All good things come to those who wait."

words = break_words(sentence)
sorted_words = sort_words(words)

print "The below should print the first word:"
print_first_word(words)
print "The below should print the last word:"
print_last_word(words)
print "The below should print the first sorted word:"
print_first_word(sorted_words)
print "The below should print the last sorted word:"
print_last_word(sorted_words)

sorted_words = sort_sentence(sentence)
print "The below should print the sorted words in a list:"
print sorted_words

print "The below should print the first and last words in the sentence:"
print_first_and_last(sentence)

print "The below should print the first and last sorted words in the sentence:"
print_first_and_last_sorted(sentence)
