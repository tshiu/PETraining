#Setting the number of people to the value 20
people = 20
#Setting the number of cats to the value 30
cats = 30 
#Setting the number of dogs to the value 15
dogs = 15

#If the below expressions are true, then it will print the string
#If not, the string will not print and we will move on to the next evaluation
if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

#Adding 5 to the previous set value for dogs, bringing dogs to 20
#Currently people = 20 and dogs = 20, so all the below statemetns will print
dogs += 5 

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs."


#SD
#1. If the expression next to if is true, then the code beneath it will run. If it
#   is false, then it will skip the code.

#2. The code needs to be indented so that python knows that the code block below 
#   belongs with the above if statement. If true, it goes to the indent. If false,
#   it will skip the block and move on to the next line that is NOT indented.

#3. It will state that there is an expected indented block. 

#4. 

if True == True:
	print "This is a true statement."

if 1 == 1 and not ("testing" == 1 or 1 == 0): 
	print "This is also true."

if 3 == 3 and not ("testing" == "testing" or "Python" == "Fun"):
	print "This will not print."

#5. If the variables are changed, the arguments will execute based on the changed values. 