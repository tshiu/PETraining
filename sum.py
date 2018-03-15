#Write a program that asks the user for a number n and writes the sum of the 
#numbers 1 to n into a file

#Ask user for the number they would like to sum
n = int(raw_input("What number would you like to sum?"))

#Setting sum to 0 to begin with
sum = 0

#Starting a loop where the number is greater than 0
#we expect this to count upwards
while(n > 0):

	#sum is now the number that was inputted
	sum = sum + n

	#should show the numbers going down by 1
	print n

	#each time n is incremented down by 1, added to the sum, until its not > 0
	n = n - 1

print (sum)


