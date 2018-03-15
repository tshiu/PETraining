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

txt.close()
txt_again.close()

#SD

#1. Done!
#2. Yep!
#3. Did this and am a bit confused around the naming but I suppose this is ok?
#4. If removed, we receive this error: name 'file_again' is not defined 

#5. 

file = raw_input("What file would you like to print?")

txt = open(file)

print "Here is the %s printed:" % txt

print txt.read () 

txt.close()

# It is probably easier to insert filename directly in the argument as it will skip a step?  

#6. Actually not quite sure how to open the file in running python. I can open them in terminal 
#.  but not in python to run. I tried python + Enter + open ex15_sample.txt 

#7. Above. 

