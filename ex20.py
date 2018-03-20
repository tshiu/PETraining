from sys import argv 

# so this tells us we will have to have two variables; include the name of the test file
script, input_file = argv 

# this function will print the entire file
# f is the argument that will be printed; it is in lieu of the file name
def print_all(f):
	print f.read() 

# seek tells you where to start in the file, if I change the 0 -> 1, 
# then it will skip over the first character, this essentially tells us that 
# rewind puts us at the very first character the in the file since it is beginning
#at 0
def rewind(f):
	f.seek(0)

# function meant to print the specified line in a file
# this will accept two arguments, the first is the line_count and the second is 
# the name of the file
def print_a_line(line_count, f):
	print line_count, f.readline()

#defining current_file as the target file of f s that we can take actions upon it
current_file = open(input_file)

print "First let's print the whole file:\n"

#calling the print_all function that will print and defining current_file(the file object
#of the input file that is called)
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# calling the rewind function that will skip to the first character of the working file 
# object 
rewind(current_file)

print "Let's print three lines:"

# setting the line count as 1, and the calling the print_a_line function that will 
# print the specified line of the file object
current_line = 1
print_a_line(current_line, current_file)

#incrementing line count by 1
#now current line is 2 
current_line += 1
print_a_line(current_line, current_file)

#incrementing line count by 1
#now current line is 3 
current_line += 1
print_a_line(current_line, current_file)

#SD

#1. yes!
#2. Yes!
#3. yes
#4. seek tells you where to start in the file, if I change the 0 -> 1, 
# then it will skip over the first character, this essentially tells us that 
# rewind puts us at the very first character the in the file since it is beginning
#5. 