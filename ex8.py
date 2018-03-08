#setting a string to call other strings
formatter = "%r %r %r %r"

#each item(?) will correspond to one of the variables and so therefore will print "1 2 3 4"
print formatter % (1, 2, 3, 4)

#will print "one two three four"
print formatter % ("one", "two", "three", "four")

#will print "True False False True"
print formatter % (True, False, False, True)

#since this does that have a new variable set, formatter originally set to 
#to that string so it will just pring that "%r %r %r %r" again
print formatter % (formatter, formatter, formatter, formatter)

#stuffs each phrase as a variable and prints it out
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)