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

# function meant to print a line in the file
# readline will go to the first line and stop when there is an enter space
# this function will simply print out line_count and the first line in the file
# each time readline is called, it will read the next line in the file as a string;
# it currently does not accept any parameters so it will iterate by 1
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

# setting the line count as 1, 
# calling print_a_line will print the argument specified and then the first line of the file
# as this is the first time the readline is called
current_line =  1
print_a_line(current_line, current_file)

# incrementing line count by 1 to now print 2
# readline is now being called again so it will increment by one and print the second line.
# this is unrelated to the current_line that is accepted as it is incrementing on its own accord
current_line += 1
print_a_line(current_line, current_file)

# incrementing line count by 1, will print 3
# readlline is being called for the third time so it will print the third line in the file
current_line += 1
print_a_line(current_line, current_file)

#SD

#1. yes!
#2. Yes!
#3. yes
#4. seek tells you where to start in the file, if I change the 0 -> 1, 
# then it will skip over the first character, this essentially tells us that 
# rewind puts us at the very first character the in the file since it is beginning
#5. Above!
