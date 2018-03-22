#setting variable people to the value 30
people = 1 
#setting the variable cars to the value 40
cars = 2
#setting the variable buses to the value 15
buses = 2

#setting an function that evaluates if cars > people is true,
#then the string below will print
if cars > people:
	print "We should take the cars."
#if cars < people, is true, the the below value will print
elif cars < people:
	print "We should not take the cars."
#for all other cases (cars = people), the below string will print. 
#(i.e. if the two expressions are both false, then this string will print)
else:
	print "We can't decide."

#setting function so that if the value of buses is greater than
#cars, then the string below will print. 
if buses > cars:
	print "That's too many buses."
#if buses < cars is evaluated as true, then the below string will print	
elif buses < cars or cars == buses: 
	print "Maybe we could take the buses."
#if the above two statements are false, then we will print the below string
else: 
	print "We still can't decide."

#if the number of people is greater than buses, then it will print "let's take
#the buses"
if people > buses:
	print "Alright, let's just take the buses."
#if thea above state is NOT true (false), then we will print the below
else:
	print "Fine, let's stay at home then."


#SD.
#1. elif, seems to just add another if statement to the code block and else seems to
#.  be a catch all for if the above statements are false.

#2. Changed the variables above.
#3. Changed the variables a bit, on line 25