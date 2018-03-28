#setting the intial variable i as 0
i = 0 

#defining an empty list of entitled numbers
numbers = []

#beginning a while loop; which states that the indented code block
#will continue to loop while the first expression maintains true

while i < 6:

	#printing the below string which calls for i to be printed within the string
	#with the first pass around, i = 0 which was definied outside the loop
	print "At the top i is %d" % i
	#this adds i (starts as 0), into the list entitled numbers
	numbers.append(i)

	#adding 1 to i the number, while this runs, with the first pass through, it is now 1
	i = i + 1 

	#will print the string "Numbers now:" followed by the list of numbers
	print "Numbers now:", numbers 
	#prining the string "at the bottom i is" followed by the new value of i which should
	#now be incremented by 1
	# at this point, i is still less than 6 so we will go back to the top of the code block
	# if i is more than 6, then we will exit the code block and move back one indentation
	print "At the bottom i is %d" % i 

#this is what the script will move onto once the while loop no longer holds true
#will print the string "The numbers"
print "The numbers: "

#creating a for loop that states, for each element/number in the list entitled numbers,
#print the item. This will look different than just typing print numberes as this will not 
#be contained in a list with brackets
for num in numbers:
	print num 


#SD
#1. Conver while-loop to a function you can call

def print_numbers_to_6():
	
	i = 0 

	the_list = []

	while i < 6:

		print "At the top is %d" % i 

		the_list.append(i)

		i = i + 1

		print "Numbers now:", numbers 

		print "At the bottom i is %d" % i 

	print "The numbers: " 

	for num in the_list:
		print num 

print_numbers_to_6()


#2. function that can try different numbers

#adding the additional parameters 
def print_numbers(start,stop):
	
	i = start 

	the_list = []

	while i < stop:

		print "At the top is %d" % i 

		the_list.append(i)

		i = i + 1

		print "Numbers now:", numbers 

		print "At the bottom i is %d" % i 

	print "The numbers: " 

	for num in the_list:
		print num 

print_numbers(2,4)

#3. function that will change the step as well 

def print_numbers_step(start,stop,step):
	
	i = start 

	the_list = []


	while i < stop:

		print "At the top is %d" % i 

		the_list.append(i)

		i = i + step

		print "Numbers now:", numbers 

		print "At the bottom i is %d" % i 

	print "The numbers: " 

	for num in the_list:
		print num 

print_numbers_step(2,10,3)

#4. Re-write using for loop and range. You do not need an incrementor because range will always just
#	increment by 1. If 

the_list = []

def print_numbers_range(start,stop):


	for i in range(start,stop):

		print "At the top is %d" % i 

		the_list.append(i)


		print "Numbers now:", the_list


		bottom_number = i + 1

		
		print "At the bottom i is %d" % bottom_number

		
		#for number in the_list:


			#print "At the bottom i is %d" % i 


print_numbers_range(0,6)











