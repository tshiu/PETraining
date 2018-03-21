#Defining the function of cheese_and_crackers 
#this will require two arguments(currently defined as cheese counta dn boxes of crackers)
def cheese_and_crackers(cheese_count, boxes_of_crackers): 

	#setting cheese count to print within this string
	print "You have %d cheeses!" % cheese_count

	#setting boxes to pring inside this string
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	
	#the \n will add an extra line between these calls
	print "Get a blanket.\n"

#we are calling the function and assigning the numbers directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "Or, we can use variables from our script:"
amount_of_cheese = 10 
amount_of_crackers = 50 

##alling the function by not assigning the numbers directly but
#assigning number to variables that are called
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"

#assigning numbers directly but letting the script do the math
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"

#calling the function by combining the variables from earlier (10, 50) and the math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


#SD
#1. 

def product(first_number, second_number):
	
	print first_number * second_number

product(10,20)

first = 10 
second = 20 

product(first, second)

product(5+5, 10+10)

product(first + first, second + second)

product(first + second, second + first)

product(first + 1, second + 2)

firstfirst = 10 + 10
secondsecond = 20 + 20 

product(firstfirst, secondsecond)

product(firstfirst + first, secondsecond + second)

product(firstfirst - second, secondsecond - first)

product(first * first, second * second)