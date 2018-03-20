# defining function named add that needs two arguments
def add (a, b):
	# first printing the two arguments in this string
	print "ADDING %d + %d" % (a, b)
	# saving this sum in return
	return a + b 

# defining function named subtract that requires two arguments
def subtract (a, b):
	# first printing the arguments in these strings
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

# calling the add function; we expect this to print the string but not 
# the actual value as it is just saving this and we haven't used
# print yet. In addition to call the value, we are setting the variables
# age, height, weight, and iq as the values that are saved from these functions
age = add(30, 5)
height = subtract(78, 4)
weight = multiply (90, 2)
iq = divide (100, 2)

#now we are actually print the values with the print command
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# setting the what variable as the combination of the values that were saved
# but also calling the functions once more
what = add(age, subtract(height, multiply(weight, divide(iq,2))))

# first is dividing IQ by 2. IQ was originally 50, so new value is 25
# second is multiply weight(180 by 25) 4500 
# third is subtract (74 - 4500) -4426
# fourth is add (-4426 + 35 ) -4391  
print "That becomes: ", what, "Can you do it by hand?"

#SD

#1. Return is similar to doing a calculation and then saving that number. It
#.  won't actually print unless it is called to print. 
#2. Above
#3. Played around with the initial value of 2 and changed the original values
#4. 

print 78 * 5 - 2 

formula = subtract( multiply(78, 5),2)

print formula 

