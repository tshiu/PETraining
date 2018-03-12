from sys import argv

#naming the script (ex15.py), and the filename you want to open
script, filename = argv

#opening the file, that returns the file object, more reading 
#on this topic
txt = open(filename)

#will print the filename
print "Here's your file %r:" % filename 
#will print the actual file
print txt.read ()

print "Type the filename again:"
#setting the filename to file_again
file_again = raw_input ("> ")

#setting txt_again to open the file that was imported
txt_again = open(file_again)

#priting the actual file again
print txt_again.read()