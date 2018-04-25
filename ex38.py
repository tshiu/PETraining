#setting the variable ten_things to this string
ten_things = "Apples Oranges Crow Telephone Light Sugar"

#printing the following string
print "Wait there's not 10 things in that list, let's fix that."

#setting stuff to a list that splits the string ten_things on spaces
#call split with ' ' on ten_things
stuff = ten_things.split(' ')

#setting more_stuff to a list that includes the following elements
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#setting a while fucntion on the list 'stuff' that runs while the length of 'stuff'
#is less than 10
while len(stuff) != 10:
	#setting variable next_one to be the last item in more_stuff list. pop will also remove
	#the last variable from the list
    next_one = more_stuff.pop()
    #printing the item that was popped after 'adding'
    print "Adding: ", next_one
    #appending the 'popped' variable which is set as next_one to the list 'stuff' 
    stuff.append(next_one)
    #printing the string with the number that indicates the number of items in stuff
    print "There's %d items now." % len(stuff)
#printing the string and the entire list 'stuff'
print "There we go: ", stuff 

print "Let's do some things with stuff."

#printing the second item in stuff
print stuff[1]
#printing the -1 item in stuff which should be the last since 0 is the first
print stuff [-1] # whoa fancy
#printing the last item in stuff
print stuff.pop()
#printing the list of stuff but 'joined'; this removes the spaces
#join stuff with '' in between them
print ''.join(stuff) # what? cool!
#joins the fourth and sixth items in the list with the '#' in the middle
print '#'.join(stuff[3:5]) # super stellar! 
#joins the third and fifth items in the stuff list with 'd' in between
print 'd'.join(stuff[2:4])

#1. Above
#2. OK
#3. Yes, object-oriented programming was confusing but I looked at the chapters ahead and took some notes
#4. This too was confusing but took notes in my notebook from the upcoming chapters.
#5. Defintion I found: Dir(something) gives you all the attributes of the object. The class is 
	#like the blueprint for the house. Not sure I completely understand, but will continue to study up on this.
