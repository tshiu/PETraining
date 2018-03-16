from sys import argv
from os.path import exists

script, from_file, to_file = argv

#stating the point of this script
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?

#opening file to play with, 
in_file = open(from_file)

#this defines indata which will be called later. read is needed
#to open the file as one big string
indata = in_file.read()

#the len function counts how long the txt is
print "The input file is %d bytes long" % len(indata)

#this line seems unneccesary
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#opening file to play, need the w so we can edit and is not just 
#in read mode
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

#SD

#1. Definition I liked: Python gets a lot of its power from the packages it installs by default and those 
#.  that you can install yourself. You can import packages to gain extra functionality. 
#Example: 

#import datetime
#oTime = datetime.datetime.now()
#print oTime.isoformat() 

#2. This just does the copying without the prompting.

from sys import argv
from os.path import exists

script, from_file, to_file = argv 

print "Copying from %s to %s" % (from_file, to_file)

#we are setting in_file as the stuff from from_file and we need to 
#first open it and then export it as a giant string as the read function does
in_file = open(from_file).read()

#we are then opening the giant string we just set as a working file and writing
#it into out_file 
out_file = open(to_file, 'w').write(in_file)

#closing files that were opened
out_file.close()
in_file.close()

#3. 

from sys import argv
script, from_file, to_file = argv

#first we open the from_file as it is in between the most parentheses; we do this 
#so that we can create an editable object that we can manipulate 
#then we are writing this opened readable file object into the to_file which is opened
#in a working mode so that we can transfer from_file's text to to_file.

#We are editing the files directly so we need to close the actual file 

open(to_file, 'w').write(open(from_file).read())

to_file.close()
from_file.close()

#4. Yes!
#5. Mac people
#6. When it opens a file, the file won't close by itself and it'll just stay open and take up resources. 
# Ref: https://stackoverflow.com/questions/36046167/is-there-a-need-to-close-files-that-have-no-reference-to-them/36063184#36063184
