#This will put the string "10" within the string x
x = "There are %d types of people." % 10 

#Sets the variable binary to the string "binary"
binary = "binary"

#Sets the variable do_not to the string "don't"
do_not = "don't"

#sets the variable y by the string "binary" (variable=binary,) 
#and "do not" (variable=do_not) within the string.
y = "Those who know %s and those who %s." % (binary, do_not)

#will print the first variable (x)
print x
#will print the second variable (y)
print y

#Will print the variable x (which is a string within this string)
print "I said: %r." % x 

#Will print the variable y (which is a string within this string)
print "I also said: '%s'. " % y

#setting the variable hilarious to false
hilarious = False

#setting the variable joke_evaluation into a string that calls another variable
joke_evaluation = "Isn't that joke so funny?! %r"

#will print the string "Isn't that joke so funny and variable 
#that is called which is hilarious which is the string false"
print joke_evaluation % hilarious

#setting these two variables as strings which will be printed one after the other
w = "This is the left side of ..."
e = "a string with a right side."

print w + e 