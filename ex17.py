from sys import argv
from os.path import exists

script, from_file, to_file = argv

#stating the point of this script
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?

#opening file to play with, 
in_file = open(from_file)

#this defines indata which will be called later. unsure why 
#the read is needed
indata = in_file.read()

#the len function counts how long the txt is
print "The input file is %d bytes long" % len(indata)

#this line seems unneccesary
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#opening file to play, need the w so we can edit and is not read
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()