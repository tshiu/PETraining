from sys import argv 

#so this tells us we will have to have two variables; include the name of the test file
script, input_file = argv 

# this function will print the entire file
def print_all(f):
	print f.read() 

#seek tells you where to start in the file, if I change the 0 -> 1, 
#then it will skip over the first character
def rewind(f):
	f.seek(0)

#  function meant to print the specified line in a file
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# currently settig the first variable as 1 and then counting up
# the start of some type of looping functionality
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)