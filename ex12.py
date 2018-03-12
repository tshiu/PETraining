age = raw_input("How old are you? ")
height = raw_input ("How tall are you? ")
weight = raw_input ("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#Study Drills
#1. pydoc raw_input 
#Help on built-in function raw_input in module __builtin__:

#raw_input(...)
    #raw_input([prompt]) -> string

#2. pydoc is a documentation generator and help system; basically like a dictionary
#3.  "%r is for debugging and is “raw representation” while %s is for display"
    