name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = "White"
hair = 'Brown'

print "Let's talk about %s." % name 
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)


#Study Drills
#1. Changed all the variables without the my above.
#2. Looked this up in google and this was the answer I received: The difference between %s and %r is that 
#   %s uses the str function and %r uses the repr function. for built-in types, the biggest difference in 
#   practice is that repr for strings includes quotes and all special characters are escaped.
#3. Looked online— https://docs.python.org/2.4/lib/typesseq-strings.html. Will reference this as it comes.
#4. 

inches = int(raw_input("What number of inches would you like to convert to cm?"))
centimeters = 0.393701 * inches

print centimeters 

pounds = int(raw_input("What number of pounds would you like to convert to kilos?"))
kilos = 2.20462 * pounds

print kilos 
