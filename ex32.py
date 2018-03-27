#setting a list entitled count that will contain the elements in the 
#brackets that are separated by the commmas. The elements contained 
#are numerical values
the_count = [1, 2, 3, 4, 5]

#setting a list entitled fruit that will contain the strings in this
#list. the elements are separated by commas 
fruits = ['apples', 'oranges', 'pears', 'apricots']

#setting a list entitled change that will contain the elements in 
#the brackets. This is a mixed group as there are both numerical values
#and strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

#setting a for-loop that executes a command on each element in a list
#this states for each number in the list 'the_count', it will call the
#element and print it within the string 
for number in the_count:
	print the_count
	print "This is count %d" % number

#setting a for-loop that executes a command on each element in a list
#this states for each element/string/fruit in the list 'fruits', it will 
#print the element inside the specified string
for fruit in fruits:
	print "A fruit of type: %s" % fruit 

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
#setting this for loop execute a command in each element in the list 
#entitled change. We are setting the variable to r because we don't know
#if it is a string or a number. Calling the element i for the same purpose.
for i in change:
		print "I got %r" % i 

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	#append function will add elements into the list that is specified in 
	#front of it. the parameter will indicate the element that should be added
	#into the specified list#elements.append(range(0,6)
	elements.append(i)



# now we can print them out too
#this for loop will execute the command on each element i, in the list entitled
#'elements'
#in this case, it will take i, and print it within the specified string
for number in elements:
	print "Element was: %d" % number


#SD
#1. Range generates a list of numbers. It has two sets of parameters. The start and the 
#.  stop will set the limits per se, e.g. range(2,10) will start at 2 and generate numbers
#,  up to the the stop number but not include it. If I included the step parameter range(2,10,2)
#.  it would could up by 2. 
#2. Yes, you can just write elements = range(0,6) 
#3. https://docs.python.org/3/tutorial/datastructures.html 
#.  append - add an item to the end of the list 
#	list.extend 
#	list.insert
#	list.remove
#	list.pop
#	list.clear
#	list.index()
#	list.count()
#	list.sort
#	list.reverse
#	list.copy