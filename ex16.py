from sys import argv

script, filename = argv

print "we're going to erase %r." % filename

#this will escape the script (control-c)
#hitting return will contine the script
print "If you don't want that, hit CTRL-C (^C)."
print "If you do what that hit RETURN."

#awaiting for the user input
raw_input("?")

#opening the file object- the w means that it is a working file
#default is r for read
print "Opening the file..."

#if you do not include the w, it will state that it is not open for
#writing later on
target = open(filename, 'w')

#I believe this erases the file; although you can add something behind
#it to indicate the size it should be truncated to
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#Setting variables for lines to later write into the file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#writing these inot the files
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."

#closes the working file
target.close()