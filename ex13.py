from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third 

#SD

#1. ValueError: need more than 1 value to unpack. It cannot run as it 
#   is looking to unpack additional variables.
#2. 

from sys import argv 

script, fruit

print "%r prints your desired fruit." % script
print "Desired fruit is %r. " % fruit 


from sys import argv 

script, fruit = argv

print "%r prints your desired fruit." % script
print "Desired fruit is %r. " % fruit 

#3. 

from sys import argv

script, fruit1, fruit2, fruit3, fruit4 = argv

print "%r prints your 4 favorite fruits."

raw_input("Would you like to continue? If so, press ENTER.")

print "Favorite fruits are %r, %r, %r, %r ." % (fruit1, fruit2, fruit3, fruit4)

#4. Yes!


