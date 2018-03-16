# this puts a tab on the line
tabby_cat = "\tI'm tabbed in."

# this 'enters' the line, puts in on a new space
persian_cat = "I'm split\non a line."

# this escapes the slashes so that the slashes will actually
# show and aren't doing a command
backslash_cat = "I'm \\ a \\ cat."

# this allows you to pring across multiple rows
# the tabs work as tabs
# the \n will enter a new line
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# this will print the above variables
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#SD 

#1.  Couldn't find index cards but found this: https://quizlet.com/13422280/python-escape-sequences-flash-cards/
#.   Will reference and study more of these items.
#2.  It does the same thing, but perhaps we would use single quotes if we wanted triple quotes in the string.
#3.  Combining variables:

sent = 'This is a sentence.'

print '''
Combining variables:
\t* Tab
\t* %r
''' % sent 

#4.  Output is "'a'" ''a'' a. The first adds single quotes, the second uses two single, the last is nothing. 

test = """
"%r" '%r' %s
"""

print test % ("a", "a", "a")
