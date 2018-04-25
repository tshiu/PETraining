#Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum of all integers from 1 to n or the product of all integers from 1 to n. Do this using a dictionary, not IF statements.



def sum(number):

	count = 0 

	while (number > 0):

		count = count + number

		number = number - 1  

	#print "The sum is %d" % count 

	return count



def factorial(number):

	pcount = 1

	while (number >= 1):

		pcount = pcount * number

		number = number - 1 

	#print "The factorial is %d" % pcount

	return pcount

n = int(raw_input("What number would you like to calculate? \n")) 

choice = str(raw_input("Would you like the sum or the factorial? \n"))



#sum(n)
#factorial(n)

#sumd = {n: sum(n)} 

#print sumd

#factd = {n: factorial(n)}

#print factd

#print choice

options = {'sum': sum(n), 'factorial': factorial(n)}

print options[choice]
